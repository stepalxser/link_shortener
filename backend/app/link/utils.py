import base64
import hashlib


def calculate_url_key(url: str, length: int= 5) -> str:
    url_hash = hashlib.sha256(url.encode())
    hash_str = base64.urlsafe_b64encode(url_hash.digest()).decode("ascii")
    return hash_str[:length]