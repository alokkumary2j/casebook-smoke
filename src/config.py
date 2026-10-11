"""Settings for the toy service."""

import os

TIMEOUT_S = int(os.environ.get("CASEBOOK_SMOKE_TIMEOUT", "10"))
RETRIES = 0
