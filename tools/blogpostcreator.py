#!/usr/bin/env python3
"""Serves blogpostcreator.html locally and opens it in your browser.

Usage:
    python3 tools/blogpostcreator.py

The "create post" button uses the File System Access API to pop a native
save dialog (Chrome/Edge only). In other browsers it falls back to a plain
download and you'll need to move the file into _posts/ yourself.
"""
import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8420
DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, fmt, *args):
        pass  # keep the console quiet


def start_server():
    port = PORT
    while port < PORT + 50:
        try:
            return socketserver.TCPServer(("localhost", port), Handler), port
        except OSError:
            port += 1
    raise RuntimeError("Could not find a free port")


def main():
    httpd, port = start_server()
    url = f"http://localhost:{port}/blogpostcreator.html"
    print(f"Blog post creator running at {url}")
    print("For the native save-location dialog, open this in Chrome or Edge.")
    print("Press Ctrl+C to stop.")
    webbrowser.open(url)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
        sys.exit(0)


if __name__ == "__main__":
    main()
