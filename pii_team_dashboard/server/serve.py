#!/usr/bin/env python3
"""Local dev server for the Pii Team Dashboard -- read + write governed-layer API.

Serves this project's pii_team_dashboard/ directory as static files (prototype/,
data/, fixtures/ -- unchanged) AND exposes:

  - read-only JSON GET endpoints over the real _governed/ layers (ledger/,
    memory/pending/, decisions/) via governed_reader.py.
  - write JSON POST endpoints for the four non-concurrence-gated console actions
    (Extract, Absorb, Archive, Elevate) via governed_writer.py. These write ONLY to
    _governed/raw/, _governed/extractions/, and (Elevate only) _governed/memory/pending/,
    and only ever create new files (see governed_writer.py's append-only-by-construction
    note). Elevate is proposal intake, never approval -- no route here, and no function
    in governed_writer.py, can write to _governed/ledger/. Ledger changes require a
    human concurrence event that happens outside this API, per the resident-context
    concurrence rule.

This server does not modify prototype/index.html; that page's fetch calls still
point at data/*.seed.json and fixtures/*.json exactly as before. Wiring the
console's buttons to these endpoints is a separate, explicitly flagged step.

Requires PyYAML (`import yaml` in governed_reader.py) on whichever interpreter
runs this script.

Run:
    python server/serve.py [port]      (default port 8765)

Then:
    http://localhost:8765/prototype/index.html   -- existing seed/fixture prototype, unchanged
    http://localhost:8765/api/state               -- real governed-layer read (ledger+pending+decisions)
    http://localhost:8765/api/ledger
    http://localhost:8765/api/pending
    http://localhost:8765/api/decisions

    POST http://localhost:8765/api/actions/extract  {"title": "...", "source_text": "...", "existing_raw_refs": ["..."], "context": "...", "topics": [...]}
    POST http://localhost:8765/api/actions/absorb   {"title": "...", "artifact_text": "...", "received_from": "..."}
    POST http://localhost:8765/api/actions/archive  {"title": "...", "dialogue_text": "..."}
    POST http://localhost:8765/api/actions/elevate  {"title": "...", "proposed_change": "...", "source": ["..."],
                                                       "confidence": "high|medium|low|contested",
                                                       "uncertainty": "...", "review_after": "YYYY-MM-DD"}
"""
from __future__ import annotations

import json
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import governed_reader as gr  # noqa: E402
import governed_writer as gw  # noqa: E402

STATIC_ROOT = Path(__file__).resolve().parent.parent  # .../pii_team_dashboard

API_ROUTES = {
    "/api/state": lambda: gr.read_state(),
    "/api/ledger": lambda: {"ledger": gr.read_ledger()},
    "/api/pending": lambda: {"pending": gr.read_pending()},
    "/api/decisions": lambda: {"decisions": gr.read_decisions()},
}

ACTION_ROUTES = {
    "/api/actions/extract": gw.extract,
    "/api/actions/absorb": gw.absorb,
    "/api/actions/archive": gw.archive,
    "/api/actions/elevate": gw.elevate,
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
            self._send_error_json(404, f"Unknown API route: {route}")
            return
        super().do_GET()

    def _serve_api(self, route: str) -> None:
        try:
            payload = API_ROUTES[route]()
        except Exception as exc:  # surface the real failure, don't swallow it
            self._send_error_json(500, f"Governed read failed: {exc.__class__.__name__}: {exc}")
            return
        self._send_json(200, payload)

    def do_POST(self):  # noqa: N802 (stdlib method name)
        route = self.path.split("?", 1)[0]
        if route not in ACTION_ROUTES:
            self._send_error_json(404, f"Unknown action route: {route}")
            return
        length = int(self.headers.get("Content-Length", 0) or 0)
        raw_body = self.rfile.read(length) if length else b"{}"
        try:
            payload = json.loads(raw_body or b"{}")
            if not isinstance(payload, dict):
                raise ValueError("request body must be a JSON object")
        except (json.JSONDecodeError, ValueError) as exc:
            self._send_error_json(400, f"Invalid JSON body: {exc}")
            return
        try:
            result = ACTION_ROUTES[route](**payload)
        except TypeError as exc:
            self._send_error_json(400, f"Bad request for {route}: {exc}")
            return
        except ValueError as exc:
            self._send_error_json(400, str(exc))
            return
        except Exception as exc:  # surface the real failure, don't swallow it
            self._send_error_json(500, f"Write failed: {exc.__class__.__name__}: {exc}")
            return
        self._send_json(201, result)

    def _send_json(self, status: int, payload) -> None:
        body = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _send_error_json(self, status: int, message: str) -> None:
        """JSON error body instead of http.server's default HTML page -- the console's
        JS client reads `error` out of the response body to log the real failure reason."""
        self._send_json(status, {"error": message})

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
