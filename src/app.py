"""A toy service that fetches a page."""

from src.config import TIMEOUT_S


def fetch(url: str) -> str:
    return f"GET {url} (timeout {TIMEOUT_S}s)"
