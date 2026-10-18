"""Send a signed test webhook, the way Paylark would (portfolio example).

Run:  python3 send_test_webhook.py              # a valid event
      python3 send_test_webhook.py --tamper     # body changed after signing
      python3 send_test_webhook.py --expired    # signed 10 minutes ago
      python3 send_test_webhook.py --duplicate  # the same event sent twice

Uses only the Python standard library.
"""

import argparse
import hashlib
import hmac
import json
import time
import urllib.error
import urllib.request
import uuid

SIGNING_SECRET = "whsec_test_portfolio"
URL = "http://127.0.0.1:5000/webhooks/paylark"


def build_event() -> dict:
    return {
        "event_id": "evt_" + uuid.uuid4().hex[:8],
        "type": "order.status_changed",
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "data": {
            "id": "ord_7Hq2KxN4Vb",
            "order_id": "shop-10045",
            "status": "completed",
            "previous_status": "initialized",
            "amount": 4995,
            "currency": "EUR",
        },
    }


def sign(body: bytes, timestamp: int) -> str:
    signed_payload = str(timestamp).encode() + b"." + body
    signature = hmac.new(SIGNING_SECRET.encode(), signed_payload, hashlib.sha256).hexdigest()
    return f"t={timestamp},v1={signature}"


def send(body: bytes, header: str) -> None:
    request = urllib.request.Request(
        URL,
        data=body,
        method="POST",
        headers={"Content-Type": "application/json", "Paylark-Signature": header},
    )
    try:
        with urllib.request.urlopen(request) as response:
            print(f"Sent. Receiver answered {response.status}")
    except urllib.error.HTTPError as error:
        print(f"Sent. Receiver answered {error.code}")
    except urllib.error.URLError:
        print("Couldn't connect. Is receiver.py running in another terminal?")


def main() -> None:
    parser = argparse.ArgumentParser(description="Send a signed Paylark test webhook.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--tamper", action="store_true", help="change the body after signing")
    group.add_argument("--expired", action="store_true", help="sign with a timestamp 10 minutes old")
    group.add_argument("--duplicate", action="store_true", help="send the same event twice")
    args = parser.parse_args()

    body = json.dumps(build_event()).encode()
    timestamp = int(time.time()) - (600 if args.expired else 0)
    header = sign(body, timestamp)

    if args.tamper:
        body = body.replace(b'"amount": 4995', b'"amount": 1')

    send(body, header)
    if args.duplicate:
        send(body, header)


if __name__ == "__main__":
    main()
