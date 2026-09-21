# Application Layer Protocol Visualizer

A dual-panel web dashboard that simulates and visualizes core application-layer network protocol exchanges (DNS, HTTP, SMTP, and HTTP Adaptive Streaming) in real time.

**🟢 Live Demo:** [https://app-layer-workflow-01.onrender.com](https://app-layer-workflow-01.onrender.com)

---

## Preview

![Application Dashboard Preview](screenshot.png)

---

## Features

* **Real-Time DNS Resolution:** Executes live socket-level DNS resolution using Python's `socket.gethostbyname()` to retrieve active public IP and CDN edge addresses for entered hostnames, with graceful fallback handling.
* **Synchronized Dual-Panel Interface:** Decouples user controls (left panel) from protocol message inspection (right panel), keeping client operations and packet flows tightly linked.
* **Interactive Playback Engine:** Full simulation playback control including **Replay**, **Step Backward**, **Pause / Resume**, and **Step Forward** to study handshakes packet by packet.
* **Defensive Parsing & Sanitization:** Uses `urllib.parse` for URL scheme/path separation and HTML character entity escaping to render protocol tags and email addresses safely without DOM corruption.

---

## Supported Protocol Simulations

| Protocol Activity | Network Protocols Involved | Flow Highlights |
| :--- | :--- | :--- |
| **HTTP Web Browsing** | DNS, HTTP/1.1 | Live A-record resolution followed by `GET` request with sanitized `Host` headers and response rendering. |
| **SMTP Mail Transfer** | DNS, SMTP | Dynamic MX record lookup, client-server handshake (`EHLO`), sender/recipient negotiation (`MAIL FROM`, `RCPT TO`), message transfer (`DATA`), and graceful termination (`QUIT`). |
| **Adaptive Video Streaming** | DNS, HTTP (HLS) | CDN edge resolution, master playlist manifest retrieval (`.m3u8`), and sequential multi-bitrate transport segment streaming (`.ts`). |

---

## Tech Stack

* **Backend:** Python 3, FastAPI, Uvicorn, Pydantic, standard library `socket` & `urllib.parse`
* **Frontend:** Vanilla HTML5, CSS3 (CSS Variables, Flexbox), Vanilla JavaScript (Fetch API, HTML5 Canvas)
* **Deployment:** Render (Web Service)

---

## Local Development Setup

### 1. Clone the repository
```bash
git clone [https://github.com/BishalRoy001/App_layer_workflow.01.git](https://github.com/BishalRoy001/App_layer_workflow.01.git)
cd App_layer_workflow.01
