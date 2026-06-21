import socket
import threading


HOST = "127.0.0.1"
PORT = 8080


def receive_request(client_socket):
    request_data = b""

    while b"\r\n\r\n" not in request_data:
        chunk = client_socket.recv(1024)

        if not chunk:
            break

        request_data += chunk

    return request_data


def parse_request(request_data):
    request_text = request_data.decode(errors="ignore")
    lines = request_text.split("\r\n")

    if len(lines) == 0:
        raise ValueError("Empty request")

    request_line = lines[0]
    parts = request_line.split()

    if len(parts) != 3:
        raise ValueError("Invalid request line")

    method, path, version = parts
    return method, path, version


def get_file_content(path):
    if path == "/":
        path = "/index.html"

    full_path = "www" + path

    with open(full_path, "rb") as file:
        return file.read()


def create_response(status_line, content_type, body):
    response = status_line.encode() + b"\r\n"
    response += b"Content-Type: " + content_type.encode() + b"\r\n"
    response += b"Content-Length: " + str(len(body)).encode() + b"\r\n"
    response += b"\r\n"
    response += body

    return response


def get_content_type(path):
    if path == "/":
        path = "/index.html"

    if path.endswith(".html"):
        return "text/html"
    elif path.endswith(".css"):
        return "text/css"
    elif path.endswith(".js"):
        return "application/javascript"
    elif path.endswith(".jpg") or path.endswith(".jpeg"):
        return "image/jpeg"
    elif path.endswith(".png"):
        return "image/png"
    elif path.endswith(".gif"):
        return "image/gif"
    elif path.endswith(".txt"):
        return "text/plain"
    elif path.endswith(".ico"):
        return "image/x-icon"
    else:
        return "application/octet-stream"


def is_allowed_path(path):
    if path == "/":
        return True

    if path.startswith("/css/"):
        return True

    if path.startswith("/images/"):
        return True

    if path.startswith("/docs/"):
        return True

    if path.startswith("/") and path.count("/") == 1:
        return True

    return False


def send_error(client_socket, status_line, message):
    body = f"<h1>{message}</h1>".encode()
    response = create_response(status_line, "text/html", body)
    client_socket.sendall(response)


def handle_client(client_socket, client_address):
    try:
        request_data = receive_request(client_socket)

        try:
            method, path, version = parse_request(request_data)


        except ValueError:
            print(f"{client_address} -> 400 Bad Request")
            send_error(
                client_socket,
                "HTTP/1.0 400 Bad Request",
                "400 Bad Request"
            )
            return

        print(
            f"{client_address} -> {method} {path} "
            f"({threading.current_thread().name})"
        )

        if method != "GET":
            send_error(
                client_socket,
                "HTTP/1.0 400 Bad Request",
                "400 Bad Request"
            )
            return

        if ".." in path:
            send_error(
                client_socket,
                "HTTP/1.0 400 Bad Request",
                "400 Bad Request"
            )
            return

        if not is_allowed_path(path):
            send_error(
                client_socket,
                "HTTP/1.0 400 Bad Request",
                "400 Bad Request"
            )
            return

        try:
            body = get_file_content(path)
            content_type = get_content_type(path)

            response = create_response(
                "HTTP/1.0 200 OK",
                content_type,
                body
            )

        except FileNotFoundError:
            response = create_response(
                "HTTP/1.0 404 Not Found",
                "text/html",
                b"<h1>404 Not Found</h1>"
            )

        client_socket.sendall(response)

    finally:
        client_socket.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server is listening on http://{HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()

    client_thread = threading.Thread(
        target=handle_client,
        args=(client_socket, client_address),
        daemon=True
    )

    client_thread.start()