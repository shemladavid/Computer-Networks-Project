# Multi-Threaded HTTP/1.0 Web Server

## Project Description

This project implements a multi-threaded HTTP/1.0 web server using Python sockets. The server handles multiple client connections concurrently using threads and serves static files from a designated directory.

Supported features:

* HTTP GET requests
* Static file serving
* Content-Type detection
* Content-Length header generation
* 200 OK responses
* 400 Bad Request responses
* 404 Not Found responses
* Directory traversal protection (`..`)
* Restricted access to approved subdirectories
* Multi-threaded client handling

## Requirements

* Python 3.x

No external dependencies are required. The project uses only Python standard library modules:

* socket
* threading

## Project Structure

```text
project/
│
├── server.py
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

## Running the Server

Open a terminal in the project directory and run:

```bash
python server.py
```

The server will start listening on:

```text
http://127.0.0.1:8080
```

## Testing

Example URLs:

```text
http://127.0.0.1:8080/
http://127.0.0.1:8080/index.html
http://127.0.0.1:8080/about.html
http://127.0.0.1:8080/css/style.css
http://127.0.0.1:8080/docs/info.txt
```

Example curl command:

```bash
curl -v http://127.0.0.1:8080/index.html
```

## Demo Video

Demo Video Link:

PASTE_YOUR_VIDEO_LINK_HERE



submit: David Shemla, Eliana Shemla and Ziv Korolker
