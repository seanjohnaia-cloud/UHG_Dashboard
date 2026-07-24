#!/usr/bin/env python3
"""Local dev server for the Pii Team Dashboard -- Checkpoint 1 (read-side wiring).

Serves this project's pii_team_dashboard/ directory as static files (prototype/,
data/, fixtures/ -- unchanged) AND exposes read-only JSON endpoints over the real
_governed/ layers (ledger/, memory/pending/, decisions/) via governed_reader.py.

This server never writes to _governed/. It does not modify prototype/index.html;
that page's fetch calls still point at data/*.seed.json and fixtures/*.json exactly
as before. Wiring the console to /api/state is a separate, explicitly flagged step.

Run:
    python server/serve.py [port]      (default port 8765)

Then:
    http://localhost:8765/prototype/index.html   -- existing seed/fixture prototype, unchanged
    http://localhost:8765/api/state               -- real governed-layer read (ledger+pending+decisions)
    http://localhost:8765/api/ledger
    http://localhost:8765/api/pending
    http://localhost:8765/api/decisions
"""
from __future__ import annotations

import json
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import governed_reader as gr  # noqa: E402

STATIC_ROOT = Path(__file__).resolve().parent.parent  # .../pii_team_dashboard

API_ROUTES = {
    "/api/state": lambda: gr.read_state(),
    "/api/ledger": lambda: {"ledger": gr.read_ledger()},
    "/api/pending": lambda: {"pending": gr.read_pending()},
    "/api/decisions": lambda: {"decisions": gr.read_decisions()},
}


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(STATIC_ROOT), **kwargs)

    def do_GET(self):  # noqa: N802 (stdlib method name)
        route = self.path.split("?", 1)[0]
        if route in API_ROUTES:
            self._serve_api(route)
            return
        if route.startswith("/api/"):
            self.send_error(404, f"Unknown API route: {route}")
            return
        super().do_GET()

    def _serve_api(self, route: str) -> None:
        try:
            payload = API_ROUTES[route]()
        except Exception as exc:  # surface the real failure, don't swallow it
            self.send_error(500, f"Governed read failed: {exc.__class__.__name__}: {exc}")
            return
        body = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt: str, *args) -> None:  # quieter, prefixed
        sys.stderr.write(f"[serve] {self.address_string()} {fmt % args}\n")


def main() -> None:
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    httpd = ThreadingHTTPServer(("localhost", port), Handler)
    print(f"Pii Team Dashboard dev server: http://localhost:{port}")
    print(f"  static (unchanged prototype): http://localhost:{port}/prototype/index.html")
    print(f"  governed read API:            http://localhost:{port}/api/state")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
