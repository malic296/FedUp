import base64, json
from datetime import datetime

def encode_cursor(sort_value: int | datetime, uuid: str) -> str:
    if isinstance(sort_value, datetime):
        raw = json.dumps({"sort": sort_value.isoformat(), "uuid": uuid})
    else:
        raw = json.dumps({"sort": sort_value, "uuid": uuid})
    return base64.urlsafe_b64encode(raw.encode()).decode()

def decode_cursor(cursor: str) -> tuple[str | int, str]:
    raw = json.loads(base64.urlsafe_b64decode(cursor).decode())
    return raw["sort"], raw["uuid"]