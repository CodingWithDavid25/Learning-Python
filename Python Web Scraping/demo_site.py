from fastapi import FastAPI, Request, Response
import time

app = FastAPI()

WINDOW_SEC = 60          # 1 minute window
MAX_REQ_PER_WINDOW = 10  # per IP

hits = {}  # ip -> list[timestamps]

def get_client_ip(request: Request) -> str:
    # If behind a reverse proxy, this may exist:
    fwd = request.headers.get("x-forwarded-for")
    if fwd:
        return fwd.split(",")[0].strip()
    # Otherwise use direct client IP:
    return request.client.host if request.client else "unknown"

@app.get("/")
def home(request: Request, response: Response):
    ip = get_client_ip(request)
    now = time.time()

    lst = hits.get(ip, [])
    lst = [t for t in lst if now - t < WINDOW_SEC]

    if len(lst) >= MAX_REQ_PER_WINDOW:
        retry_after = 15
        response.headers["Retry-After"] = str(retry_after)
        return Response(
            content=f"429 Too Many Requests (ip={ip})\n",
            status_code=429,
            media_type="text/plain",
        )

    lst.append(now)
    hits[ip] = lst

    html = """
    <html><body>
      <div class="quote"><span class="text">"Scraping is just parsing HTML."</span>
        <small class="author">David</small>
      </div>
      <div class="quote"><span class="text">"Rate limits are often IP-based."</span>
        <small class="author">Server</small>
      </div>
    </body></html>
    """
    return Response(content=html, media_type="text/html")
