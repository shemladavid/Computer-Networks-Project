# Multi-Threaded HTTP Web Server

## Submitted By

* David Shemla
* Eliana Shemla
* Ziv Korolker

## Course Information

Computer Networks – Programming Assignment
Bar-Ilan University
Submission Date: July 2026

---

## Project Description

This project implements a multi-threaded HTTP web server in Python using low-level sockets and threads.

The server supports:

* Serving static files from a local `www` directory.
* Handling multiple client connections concurrently using threads.
* Returning appropriate HTTP status codes (`200`, `400`, and `404`).
* Blocking directory traversal attacks (`../`).
* Logging client requests and server responses.
* Supporting multiple file types including HTML, CSS, images, and text files.

---

## Features

### Multi-threaded Architecture

Each client connection is handled in a separate thread, allowing multiple clients to be served simultaneously.

### Static File Serving

The server serves files located inside the `www` directory.

Supported file types include:

* `.html`
* `.css`
* `.png`
* `.jpg`
* `.jpeg`
* `.txt`

### HTTP Status Codes

The server correctly returns:

* `200 OK`
* `400 Bad Request`
* `404 Not Found`

### Security

The implementation prevents directory traversal attacks by rejecting requests containing:

```text
..
```

Only files inside approved directories may be accessed.

---

## Project Structure

```text
Computer-Networks-Project/
│
├── server.py
├── README.md
│
└── www/
    ├── index.html
    ├── about.html
    ├── css/
    │   └── style.css
    ├── images/
    │   └── logo.png
    └── docs/
        └── info.txt
```

---

## Requirements

* Python 3.10 or newer.
* No external libraries are required.

The project uses only Python standard library modules:

```python
socket
threading
os
time
mimetypes
```

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/shemladavid/Computer-Networks-Project.git
cd Computer-Networks-Project
```

Run the server:

```bash
python server.py
```

The server starts on:

```text
http://127.0.0.1:8080
```

---

## Example Requests

Open the following URLs in a browser:

```text
http://127.0.0.1:8080/
http://127.0.0.1:8080/about.html
http://127.0.0.1:8080/css/style.css
http://127.0.0.1:8080/images/logo.png
http://127.0.0.1:8080/docs/info.txt
```

---

## Testing Error Handling

### 404 Not Found

```bash
curl -v http://127.0.0.1:8080/missing.html
```

Expected response:

```text
HTTP/1.1 404 Not Found
```

---

### 400 Bad Request

```bash
printf "INVALID REQUEST\r\n\r\n" | nc 127.0.0.1 8080
```

Expected response:

```text
HTTP/1.1 400 Bad Request
```

---

### Directory Traversal Protection

```bash
curl -v http://127.0.0.1:8080/../../secret.txt
```

Expected response:

```text
HTTP/1.1 400 Bad Request
```

---

## Demonstrating Concurrent Connections

Open two terminals and execute:

Terminal 1:

```bash
curl http://127.0.0.1:8080/
```

Terminal 2:

```bash
curl http://127.0.0.1:8080/about.html
```

Both requests should be processed simultaneously by different threads.

---

## Demo Video

https://youtu.be/PASkgvK_d5I

The demonstration includes:

* Starting the server.
* Serving static files.
* Concurrent client connections.
* Returning 404 responses.
* Returning 400 responses.
* Blocking directory traversal attacks.
* Server logging output.

---

## Academic Integrity

This project was developed independently in accordance with the course academic integrity guidelines.

No code from other students or groups was used.
