from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from urllib.parse import urlparse
import socket

app = FastAPI()

class BrowseReq(BaseModel): url: str
class MailReq(BaseModel): to_email: str; subject: str; body: str
class StreamReq(BaseModel): quality: str

# Helper to keep sequence dictionaries DRY and readable
def step(direction, sender, receiver, protocol, text):
    return {"type": direction, "sender": sender, "receiver": receiver, "protocol": protocol, "msg": text}

@app.get("/")
def serve_ui():
    return FileResponse("index.html")

@app.post("/api/browse")
def browse(data: BrowseReq):
    url = data.url.strip()
    if not url.startswith(("http://", "https://")):
        url = "http://" + url
        
    p = urlparse(url)
    host = p.netloc or "example.com"
    path = (p.path or "/") + ("?" + p.query if p.query else "")

    try:
        ip = socket.gethostbyname(host)
    except:
        ip = "192.0.2.1" # Fallback for invalid domains

    return {"sequence": [
        step("out", "CLIENT", "DNS SERVER", "DNS", f"Query A Record: {host}"),
        step("in", "DNS SERVER", "CLIENT", "DNS", f"Response: {ip}"),
        step("out", "CLIENT", "WEB SERVER", "HTTP", f"GET {path} HTTP/1.1\nHost: {host}\nAccept: text/html"),
        step("in", "WEB SERVER", "CLIENT", "HTTP", "HTTP/1.1 200 OK\nContent-Type: text/html\n\n[HTML Document Payload]")
    ]}

@app.post("/api/mail")
def mail(data: MailReq):
    parts = data.to_email.split('@')
    domain = parts[1] if len(parts) > 1 else "local.edu"
    
    return {"sequence": [
        step("out", "CLIENT", "DNS SERVER", "DNS", f"Query MX Record: {domain}"),
        step("in", "DNS SERVER", "CLIENT", "DNS", f"Response: mail.{domain}"),
        step("out", "CLIENT", "SMTP SERVER", "SMTP", "EHLO client.local"),
        step("in", "SMTP SERVER", "CLIENT", "SMTP", f"250-mail.{domain} Hello\n250-8BITMIME\n250 OK"),
        step("out", "CLIENT", "SMTP SERVER", "SMTP", "MAIL FROM: <student@university.edu>"),
        step("in", "SMTP SERVER", "CLIENT", "SMTP", "250 2.1.0 OK"),
        step("out", "CLIENT", "SMTP SERVER", "SMTP", f"RCPT TO: <{data.to_email}>"),
        step("in", "SMTP SERVER", "CLIENT", "SMTP", "250 2.1.5 OK"),
        step("out", "CLIENT", "SMTP SERVER", "SMTP", "DATA"),
        step("in", "SMTP SERVER", "CLIENT", "SMTP", "354 End data with <CR><LF>.<CR><LF>"),
        step("out", "CLIENT", "SMTP SERVER", "SMTP", f"Subject: {data.subject}\n\n{data.body}\n."),
        step("in", "SMTP SERVER", "CLIENT", "SMTP", "250 2.0.0 Ok: queued as 7F3B1C"),
        step("out", "CLIENT", "SMTP SERVER", "SMTP", "QUIT"),
        step("in", "SMTP SERVER", "CLIENT", "SMTP", "221 2.0.0 Bye")
    ]}

@app.post("/api/stream")
def stream(data: StreamReq):
    cdn = "cdn.stream.com"
    try:
        ip = socket.gethostbyname(cdn)
    except:
        ip = "198.51.100.14"

    return {"sequence": [
        step("out", "CLIENT", "DNS SERVER", "DNS", f"Query A Record: {cdn}"),
        step("in", "DNS SERVER", "CLIENT", "DNS", f"Response: {ip}"),
        step("out", "CLIENT", "VIDEO SERVER", "HTTP", f"GET /master_manifest.m3u8 HTTP/1.1\nHost: {cdn}"),
        step("in", "VIDEO SERVER", "CLIENT", "HTTP", "HTTP/1.1 200 OK\nContent-Type: application/vnd.apple.mpegurl\n\n[Manifest Data]"),
        step("out", "CLIENT", "VIDEO SERVER", "HTTP", f"GET /segments/{data.quality}/seg_001.ts HTTP/1.1\nHost: {cdn}"),
        step("in", "VIDEO SERVER", "CLIENT", "HTTP", "HTTP/1.1 200 OK\nContent-Type: video/mp2t\n\n[Binary Video Data]"),
        step("out", "CLIENT", "VIDEO SERVER", "HTTP", f"GET /segments/{data.quality}/seg_002.ts HTTP/1.1\nHost: {cdn}"),
        step("in", "VIDEO SERVER", "CLIENT", "HTTP", "HTTP/1.1 200 OK\nContent-Type: video/mp2t\n\n[Binary Video Data]")
    ]}
