"""Module entrypoint for `python3 -m hawking`."""

from __future__ import annotations

from .cli import main

if __name__ == "__main__":
    raise SystemExit(main())
