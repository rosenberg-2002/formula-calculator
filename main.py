"""
Formula Calculator — Web UI
Serves a local web interface and handles formula calculations via a JSON API.
Run:  python main.py
"""

import http.server
import json
import os
import threading
import webbrowser
from formulas import FORMULAS, calculate_formula

PORT = 5050

# ── Category mapping (UI-only metadata) ─────────────────────────────────────
CATEGORIES = {
    "Quadratic Equation":              "Algebra",
    "Pythagorean Theorem":             "Geometry",
    "Circle Area":                     "Geometry",
    "Rectangle Area":                  "Geometry",
    "Triangle Area (Heron's Formula)": "Geometry",
    "Sphere Volume":                   "Geometry",
    "Distance Formula":                "Geometry",
    "Simple Interest":                 "Finance",
    "Compound Interest":               "Finance",
    "Celsius to Fahrenheit":           "Temperature",
    "Fahrenheit to Celsius":           "Temperature",
    "Body Mass Index (BMI)":           "Health",
    "Kinetic Energy":                  "Physics",
    "Ohm's Law":                       "Physics",
    "Power (Electrical)":              "Physics",
    "Percentage":                      "Math",
}


def _formulas_payload():
    return {
        name: {
            "description": info["description"],
            "parameters":  info["parameters"],
            "output_unit": info["output_unit"],
            "category":    CATEGORIES.get(name, "Other"),
        }
        for name, info in FORMULAS.items()
    }


class _Handler(http.server.BaseHTTPRequestHandler):

    _base = os.path.dirname(os.path.abspath(__file__))

    # ── GET ──────────────────────────────────────────────────────────────────
    def do_GET(self):
        routes = {
            "/":              ("index.html", "text/html; charset=utf-8"),
            "/index.html":    ("index.html", "text/html; charset=utf-8"),
            "/style.css":     ("style.css",  "text/css; charset=utf-8"),
        }
        if self.path in routes:
            fname, ctype = routes[self.path]
            self._file(os.path.join(self._base, fname), ctype)
        elif self.path == "/api/formulas":
            self._json(200, _formulas_payload())
        else:
            self._respond(404, "text/plain", b"Not found")

    # ── POST ─────────────────────────────────────────────────────────────────
    def do_POST(self):
        if self.path != "/api/calculate":
            self._respond(404, "text/plain", b"Not found")
            return

        length = int(self.headers.get("Content-Length", 0))
        body   = self.rfile.read(length)
        try:
            payload = json.loads(body)
            name    = payload["formula"]
            values  = {k: float(v) for k, v in payload["values"].items()}
            result  = calculate_formula(name, values)
            unit    = FORMULAS[name]["output_unit"]
            self._json(200, {"result": round(result, 8), "unit": unit})
        except (ValueError, KeyError) as exc:
            self._json(400, {"error": str(exc)})
        except Exception as exc:
            self._json(500, {"error": f"Calculation error: {exc}"})

    # ── Helpers ───────────────────────────────────────────────────────────────
    def _file(self, path, content_type):
        try:
            with open(path, "rb") as fh:
                data = fh.read()
            self._respond(200, content_type, data)
        except FileNotFoundError:
            self._respond(404, "text/plain", b"File not found")

    def _json(self, status, obj):
        data = json.dumps(obj).encode()
        self._respond(status, "application/json", data)

    def _respond(self, status, content_type, body):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", len(body))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *_):
        pass  # suppress access logs


# ── Entry point ───────────────────────────────────────────────────────────────
def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server = http.server.HTTPServer(("127.0.0.1", PORT), _Handler)
    url    = f"http://127.0.0.1:{PORT}"
    threading.Timer(0.4, lambda: webbrowser.open(url)).start()
    print(f"Formula Calculator  →  {url}  (Ctrl+C to quit)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
        server.shutdown()


if __name__ == "__main__":
    main()
