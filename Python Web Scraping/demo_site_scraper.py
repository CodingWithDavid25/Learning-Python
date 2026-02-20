import time
import random
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

init(autoreset=True)

URL = "https://hammer-employee-sentences-gates.trycloudflare.com/" #https://hammer-employee-sentences-gates.trycloudflare.com/

USE_PROXY = True
PROXY_POOL = [
    "http://codingwithdavid-US:3MeSPO10F312@geo.ipcook.com:32345",
    "http://codingwithdavid1-US:3MeSPO10F313@geo.ipcook.com:32345",
]

GREEN = Fore.GREEN + Style.BRIGHT
RED = Fore.RED + Style.BRIGHT
YELLOW = Fore.YELLOW + Style.BRIGHT
RESET = Style.RESET_ALL


def pick_proxy(i: int):
    if not USE_PROXY or not PROXY_POOL:
        return None
    p = PROXY_POOL[(i - 1) % len(PROXY_POOL)]
    return {"http": p, "https": p}


# ---- resilient session ----
session = requests.Session()
session.headers.update({
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "close",  # helps with flaky proxy tunnels / SSL EOFs
})

retry_cfg = Retry(
    total=3,
    connect=3,
    read=3,
    backoff_factor=0.8,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"],
    raise_on_status=False,
)

adapter = HTTPAdapter(max_retries=retry_cfg, pool_connections=10, pool_maxsize=10)
session.mount("http://", adapter)
session.mount("https://", adapter)


def test_proxies():
    if not USE_PROXY or not PROXY_POOL:
        print("proxy OFF")
        return

    for idx, p in enumerate(PROXY_POOL):
        try:
            r = session.get(
                "https://httpbin.org/ip",
                proxies={"http": p, "https": p},
                timeout=(10, 20),
            )
            r.raise_for_status()
            ip = r.json().get("origin", r.text.strip())
            print(f"proxy #{idx} -> OK: {ip}")
        except Exception as e:
            print(f"proxy #{idx} -> FAIL: {type(e).__name__}")


def fetch(i: int):
    # retries for TLS/proxy flakiness (SSLEOF, ProxyError, timeouts, resets)
    for attempt in range(1, 5):
        proxies = pick_proxy(i + attempt - 1)

        try:
            r = session.get(URL, proxies=proxies, timeout=(10, 20))
        except (
            requests.exceptions.SSLError,
            requests.exceptions.ProxyError,
            requests.exceptions.ConnectTimeout,
            requests.exceptions.ReadTimeout,
            requests.exceptions.ConnectionError,
        ) as e:
            print(f"{YELLOW}[{i}] {type(e).__name__} (retry {attempt}/4){RESET}")
            time.sleep(0.8 * attempt + random.uniform(0.1, 0.6))
            continue

        # Respect Retry-After on rate limit
        if r.status_code == 429:
            wait = int(r.headers.get("Retry-After", "5"))
            print(f"{RED}[{i}] 429{RESET} (wait {wait}s)")
            time.sleep(wait + random.uniform(0.5, 1.5))
            return None

        # Common "blocked/challenged" statuses
        if r.status_code in (403, 407, 503, 520, 521, 522, 523, 524):
            print(f"{YELLOW}[{i}] {r.status_code} blocked/challenged{RESET}")
            return None

        try:
            r.raise_for_status()
        except requests.HTTPError:
            print(f"{YELLOW}[{i}] HTTP {r.status_code}{RESET}")
            return None

        return r.text

    # all retries failed
    return None


def parse(html: str):
    soup = BeautifulSoup(html, "html.parser")
    rows = []
    for q in soup.select(".quote"):
        a = q.select_one(".author")
        t = q.select_one(".text")
        if a and t:
            rows.append((a.get_text(strip=True), t.get_text(strip=True)))
    return rows


def main():
    test_proxies()

    ok = blocked = 0
    for i in range(1, 40):
        time.sleep(random.uniform(0.6, 1.4))  # slightly slower = fewer bans/EOFs
        html = fetch(i)

        if not html:
            blocked += 1
            continue

        rows = parse(html)
        ok += 1
        print(f"{GREEN}[{i}] 200 OK {RESET}— {len(rows)} quotes")

    print(f"\nDONE: {GREEN}OK={ok}{RESET}, {RED}blocked={blocked}{RESET}")


if __name__ == "__main__":
    main()
