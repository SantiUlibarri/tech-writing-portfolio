"""Paylark webhook receiver (portfolio example).

Listens for Paylark webhooks, verifies the Paylark-Signature header,
ignores duplicate events, and responds 200 quickly.

Run:  python3 receiver.py
Uses only the Python standard library.
"""

import hashlib
import hmac
import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

SIGNING_SECRET = "whsec_test_portfolio"  # In production, read this from an environment variable.
TOLERANCE_SECONDS = 300                   # Reject events signed more than 5 minutes ago.
PORT = 5000

seen_event_ids = set()  # In production, store these in a database.


def verify_signature(raw_body: bytes, header: str) -> bool:
    """Return True if the Paylark-Signature header matches the raw body."""
    try:
        parts = dict(item.split("=", 1) for item in header.split(","))
        timestamp = parts["t"]
        received_signature = parts["v1"]
    except (KeyError, ValueError):
        return False

    if abs(time.time() - int(timestamp)) > TOLERANCE_SECONDS:
        return False

    signed_payload = timestamp.encode() + b"." + raw_body
    expected_signature = hmac.new(
        SIGNING_SECRET.encode(), signed_payload, hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(expected_signature, received_signature)


class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/webhooks/paylark":
            self.send_response(404)
            self.end_headers()
            return

        raw_body = self.rfile.read(int(self.headers.get("Content-Length", 0)))
        header = self.headers.get("Paylark-Signature", "")

        if not verify_signature(raw_body, header):
            print("✗ Rejected: invalid or expired signature")
            self.send_response(400)
            self.end_headers()
            return

        event = json.loads(raw_body)
        if event["event_id"] in seen_event_ids:
            print(f"↺ Duplicate {event['event_id']}: already processed, ignoring")
            self.send_response(200)
            self.end_headers()
            return

        seen_event_ids.add(event["event_id"])
        data = event["data"]
        print(
            f"✓ Verified {event['event_id']}: order {data['order_id']} "
            f"{data['previous_status']} → {data['status']}"
        )
        self.send_response(200)
        self.end_headers()

    def log_message(self, *args):
        pass  # Keep the terminal output to our own messages.


if __name__ == "__main__":
    print(f"Listening on http://127.0.0.1:{PORT}/webhooks/paylark  (Ctrl+C to stop)")
    HTTPServer(("127.0.0.1", PORT), WebhookHandler).serve_forever()
