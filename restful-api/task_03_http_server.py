#!/usr/bin/python3
"""The http.server module in Python’s standard library provides
basic classes for implementing web servers"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class MyRequestHandler(BaseHTTPRequestHandler):
    """Handles HTTP GET requests"""

    def do_GET(self):
        """Handles GET request"""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response_data = {"name": "John", "age": 30, "city": "New York"}

            self.wfile.write(json.dumps(response_data).encode('utf-8'))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode("utf-8"))

        else:
             self.send_response(404)
             self.send_header("Content-type", "application/json")
             self.end_headers()
             error_message = {"error": "Endpoint not found"}
             self.wfile.write(json.dumps(error_message).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=MyRequestHandler, port=8000):
    """Start the HTTP server."""
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on http://localhost:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by user.")
    finally:
        httpd.server_close()
        print("Server closed.")


if __name__ == "__main__":
    run()
