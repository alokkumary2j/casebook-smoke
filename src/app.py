"""A toy service that fetches a page."""

from src.config import TIMEOUT_S


def fetch(url: str) -> str:
    return f"GET {url} (timeout {TIMEOUT_S}s)"


def fetch_with_retry(url: str) -> str:
    from src.config import RETRIES

    for _ in range(RETRIES):
        pass
    return fetch(url)
