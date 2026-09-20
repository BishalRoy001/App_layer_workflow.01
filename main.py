from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from urllib.parse import urlparse
import socket

app = FastAPI()

# Serve the frontend UI
@app.get("/")
async def serve_ui():
    return FileResponse("index.html")

# Define strict data models for security and validation
class BrowseRequest(BaseModel):
    url: str

class MailRequest(BaseModel):
    to_email: str
    subject: str
    body: str

class StreamRequest(BaseModel):
    quality: str

# Protocol Endpoints
@app.post("/api/browse")
async def browse(data: BrowseRequest):
    raw_url = data.url.strip()
    
    # Auto-inject scheme if user forgot it
    if not raw_url.startswith("http://") and not raw_url.startswith("https://"):
        raw_url = "http://" + raw_url
        
    parsed = urlparse(raw_url)
    hostname = parsed.netloc or "example.com"
    
    # Reconstruct path and query for the HTTP request
    path = parsed.path if parsed.path else "/"
    if parsed.query:
        path += "?" + parsed.query

    # Live DNS Resolution with safe fallback
    try:
        resolved_ip = socket.gethostbyname(hostname)
    except Exception:
        resolved_ip = "192.0.2.1" # Standard documentation placeholder IP

    sequence = [
        {"type": "out", "sender": "CLIENT", "receiver": "DNS SERVER", "protocol": "DNS", "msg": f"Query A Record: {hostname}"},
        {"type": "in", "sender": "DNS SERVER", "receiver": "CLIENT", "protocol": "DNS", "msg": f"Response: {resolved_ip}"},
        {"type": "out", "sender": "CLIENT", "receiver": "WEB SERVER", "protocol": "HTTP", "msg": f"GET {path} HTTP/1.1\nHost: {hostname}\nAccept: text/html"},
        {"type": "in", "sender": "WEB SERVER", "receiver": "CLIENT", "protocol": "HTTP", "msg": "HTTP/1.1 200 OK\nContent-Type: text/html\n\n[HTML Document Payload]"}
    ]
    return {"sequence": sequence}

@app.post("/api/mail")
async def mail(data: MailRequest):
    # Extract the domain dynamically for the MX lookup
    email_parts = data.to_email.split('@')
    domain = email_parts[1] if len(email_parts) > 1 else "local.edu"
    
    sequence = [
        {"type": "out", "sender": "CLIENT", "receiver": "DNS SERVER", "protocol": "DNS", "msg": f"Query MX Record: {domain}"},
        {"type": "in", "sender": "DNS SERVER", "receiver": "CLIENT", "protocol": "DNS", "msg": f"Response: mail.{domain}"},
        {"type": "out", "sender": "CLIENT", "receiver": "SMTP SERVER", "protocol": "SMTP", "msg": "EHLO client.local"},
        {"type": "in", "sender": "SMTP SERVER", "receiver": "CLIENT", "protocol": "SMTP", "msg": f"250-mail.{domain} Hello\n250-8BITMIME\n250 OK"},
        {"type": "out", "sender": "CLIENT", "receiver": "SMTP SERVER", "protocol": "SMTP", "msg": "MAIL FROM: <student@university.edu>"},
        {"type": "in", "sender": "SMTP SERVER", "receiver": "CLIENT", "protocol": "SMTP", "msg": "250 2.1.0 OK"},
        {"type": "out", "sender": "CLIENT", "receiver": "SMTP SERVER", "protocol": "SMTP", "msg": f"RCPT TO: <{data.to_email}>"},
        {"type": "in", "sender": "SMTP SERVER", "receiver": "CLIENT", "protocol": "SMTP", "msg": "250 2.1.5 OK"},
        {"type": "out", "sender": "CLIENT", "receiver": "SMTP SERVER", "protocol": "SMTP", "msg": "DATA"},
        {"type": "in", "sender": "SMTP SERVER", "receiver": "CLIENT", "protocol": "SMTP", "msg": "354 End data with <CR><LF>.<CR><LF>"},
        {"type": "out", "sender": "CLIENT", "receiver": "SMTP SERVER", "protocol": "SMTP", "msg": f"Subject: {data.subject}\n\n{data.body}\n."},
        {"type": "in", "sender": "SMTP SERVER", "receiver": "CLIENT", "protocol": "SMTP", "msg": "250 2.0.0 Ok: queued as 7F3B1C"},
        {"type": "out", "sender": "CLIENT", "receiver": "SMTP SERVER", "protocol": "SMTP", "msg": "QUIT"},
        {"type": "in", "sender": "SMTP SERVER", "receiver": "CLIENT", "protocol": "SMTP", "msg": "221 2.0.0 Bye"}
    ]
    return {"sequence": sequence}

@app.post("/api/stream")
async def stream(data: StreamRequest):
    cdn_hostname = "cdn.stream.com"
    
    try:
        resolved_ip = socket.gethostbyname(cdn_hostname)
    except Exception:
        resolved_ip = "198.51.100.14"

    sequence = [
        {"type": "out", "sender": "CLIENT", "receiver": "DNS SERVER", "protocol": "DNS", "msg": f"Query A Record: {cdn_hostname}"},
        {"type": "in", "sender": "DNS SERVER", "receiver": "CLIENT", "protocol": "DNS", "msg": f"Response: {resolved_ip}"},
        {"type": "out", "sender": "CLIENT", "receiver": "VIDEO SERVER", "protocol": "HTTP", "msg": "GET /master_manifest.m3u8 HTTP/1.1\nHost: cdn.stream.com"},
        {"type": "in", "sender": "VIDEO SERVER", "receiver": "CLIENT", "protocol": "HTTP", "msg": "HTTP/1.1 200 OK\nContent-Type: application/vnd.apple.mpegurl\n\n[Manifest Data]"},
        {"type": "out", "sender": "CLIENT", "receiver": "VIDEO SERVER", "protocol": "HTTP", "msg": f"GET /segments/{data.quality}/seg_001.ts HTTP/1.1\nHost: cdn.stream.com"},
        {"type": "in", "sender": "VIDEO SERVER", "receiver": "CLIENT", "protocol": "HTTP", "msg": "HTTP/1.1 200 OK\nContent-Type: video/mp2t\n\n[Binary Video Data]"},
        {"type": "out", "sender": "CLIENT", "receiver": "VIDEO SERVER", "protocol": "HTTP", "msg": f"GET /segments/{data.quality}/seg_002.ts HTTP/1.1\nHost: cdn.stream.com"},
        {"type": "in", "sender": "VIDEO SERVER", "receiver": "CLIENT", "protocol": "HTTP", "msg": "HTTP/1.1 200 OK\nContent-Type: video/mp2t\n\n[Binary Video Data]"}
    ]
    return {"sequence": sequence}
