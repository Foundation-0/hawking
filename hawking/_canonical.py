"""Single shared canonical JSON serialization & SHA-256 receipt hashing.

Every hawking module (run_all / build_certificate payloads and module main() emitters) and
the unified CLI (hawking.cli) serialize and hash through these helpers, so a digest computed
anywhere is a digest over byte-identical canonical text. Canonical form: JSON with sorted
keys, 2-space indent, allow_nan=False, UTF-8, terminated by exactly one trailing newline.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any, Dict, Tuple

RECEIPT_KEY = "canonical_sha256"


def canonical_json(payload: Any) -> str:
    """Canonical receipt text for a JSON-serializable payload."""
    return json.dumps(payload, indent=2, sort_keys=True, allow_nan=False) + "\n"


def canonical_digest(payload: Any) -> Tuple[str, str]:
    """Return (canonical text, its SHA-256 hex digest)."""
    text = canonical_json(payload)
    return text, hashlib.sha256(text.encode("utf-8")).hexdigest()


def embed_canonical_sha256(payload: Dict[str, Any], key: str = RECEIPT_KEY) -> str:
    """Embed the payload's canonical SHA-256 under `key` and return it.

    The digest is computed over the canonical text of the payload WITHOUT the receipt key
    itself (a self-referential digest is impossible), then stored into the payload.
    """
    base = {k: v for k, v in payload.items() if k != key}
    _text, digest = canonical_digest(base)
    payload[key] = digest
    return digest
