from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from urllib.parse import urlparse
import socket  # Added to perform real DNS lookups

app = FastAPI()

class BrowseRequest(BaseModel):
    url: str

class MailRequest(BaseModel):
    to_email: str
    subject: str
    body: str

class StreamRequest(BaseModel):
    quality: str

@app.get("/")
def serve_frontend():
    return FileResponse("index.html")

@app.post("/api/browse")
def simulate_browse(req: BrowseRequest):
    # Extract just the domain name (e.g., www.youtube.com)
    domain = urlparse(req.url).netloc or req.url
    
    # Dynamically resolve the real IP address!
    try:
        resolved_ip = socket.gethostbyname(domain)
    except socket.gaierror:
        # Fallback to a default IP if the domain is fake or offline
        resolved_ip = "93.184.216.34" 
        
    return {
        "sequence": [
            {"sender": "Client", "receiver": "DNS Server", "protocol": "DNS", "msg": f"Query A Record: {domain}", "type": "out"},
            {"sender": "DNS Server", "receiver": "Client", "protocol": "DNS", "msg": f"Response: {resolved_ip}", "type": "in"},
            {"sender": "Client", "receiver": "Web Server", "protocol": "HTTP", "msg": f"GET / HTTP/1.1\nHost: {domain}\nAccept: text/html", "type": "out"},
            {"sender": "Web Server", "receiver": "Client", "protocol": "HTTP", "msg": "HTTP/1.1 200 OK\nContent-Type: text/html\n\n<!DOCTYPE html>...", "type": "in"}
        ]
    }

@app.post("/api/mail")
def simulate_mail(req: MailRequest):
    domain = req.to_email.split('@')[-1] if '@' in req.to_email else "university.edu"
    return {
        "sequence": [
            {"sender": "Client", "receiver": "DNS Server", "protocol": "DNS", "msg": f"Query MX Record: {domain}", "type": "out"},
            {"sender": "DNS Server", "receiver": "Client", "protocol": "DNS", "msg": f"Response: mail.{domain}", "type": "in"},
            {"sender": "Client", "receiver": "SMTP Server", "protocol": "SMTP", "msg": "EHLO client.local", "type": "out"},
            {"sender": "SMTP Server", "receiver": "Client", "protocol": "SMTP", "msg": "250-mail.server.com Hello\n250-8BITMIME\n250 OK", "type": "in"},
            {"sender": "Client", "receiver": "SMTP Server", "protocol": "SMTP", "msg": "MAIL FROM: <student@local.com>", "type": "out"},
            {"sender": "SMTP Server", "receiver": "Client", "protocol": "SMTP", "msg": "250 2.1.0 OK", "type": "in"},
            {"sender": "Client", "receiver": "SMTP Server", "protocol": "SMTP", "msg": f"RCPT TO: <{req.to_email}>", "type": "out"},
            {"sender": "SMTP Server", "receiver": "Client", "protocol": "SMTP", "msg": "250 2.1.5 OK", "type": "in"},
            {"sender": "Client", "receiver": "SMTP Server", "protocol": "SMTP", "msg": "DATA", "type": "out"},
            {"sender": "SMTP Server", "receiver": "Client", "protocol": "SMTP", "msg": "354 End data with <CR><LF>.<CR><LF>", "type": "in"},
            {"sender": "Client", "receiver": "SMTP Server", "protocol": "SMTP", "msg": f"Subject: {req.subject}\n\n{req.body}\n.", "type": "out"},
            {"sender": "SMTP Server", "receiver": "Client", "protocol": "SMTP", "msg": "250 2.0.0 Ok: queued as 7F3B1C", "type": "in"},
            {"sender": "Client", "receiver": "SMTP Server", "protocol": "SMTP", "msg": "QUIT", "type": "out"},
            {"sender": "SMTP Server", "receiver": "Client", "protocol": "SMTP", "msg": "221 2.0.0 Bye", "type": "in"}
        ]
    }

@app.post("/api/stream")
def simulate_stream(req: StreamRequest):
    return {
        "sequence": [
            {"sender": "Client", "receiver": "DNS Server", "protocol": "DNS", "msg": "Query A Record: cdn.stream.com", "type": "out"},
            {"sender": "DNS Server", "receiver": "Client", "protocol": "DNS", "msg": "Response: 198.51.100.14", "type": "in"},
            {"sender": "Client", "receiver": "Video Server", "protocol": "HTTP", "msg": "GET /master_manifest.m3u8 HTTP/1.1", "type": "out"},
            {"sender": "Video Server", "receiver": "Client", "protocol": "HTTP", "msg": "HTTP/1.1 200 OK\nContent-Type: application/vnd.apple.mpegurl", "type": "in"},
            {"sender": "Client", "receiver": "Video Server", "protocol": "HTTP", "msg": f"GET /segments/{req.quality}/seg_001.ts HTTP/1.1", "type": "out"},
            {"sender": "Video Server", "receiver": "Client", "protocol": "HTTP", "msg": "HTTP/1.1 200 OK\nContent-Type: video/mp2t\n[Binary Video Data]", "type": "in"},
            {"sender": "Client", "receiver": "Video Server", "protocol": "HTTP", "msg": f"GET /segments/{req.quality}/seg_002.ts HTTP/1.1", "type": "out"},
            {"sender": "Video Server", "receiver": "Client", "protocol": "HTTP", "msg": "HTTP/1.1 200 OK\nContent-Type: video/mp2t\n[Binary Video Data]", "type": "in"}
        ]
    }