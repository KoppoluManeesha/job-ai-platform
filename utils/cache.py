import hashlib
import json
import os

CACHE_FILE = "cache.json"


def load_cache():
    try:
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, "r") as f:
                content = f.read().strip()
                if not content:
                    return {}
                return json.loads(content)
        return {}
    except:
        return {}


def save_cache(cache):
    try:
        with open(CACHE_FILE, "w") as f:
            json.dump(cache, f)
    except:
        pass


def get_hash(text):
    return hashlib.md5(text.encode()).hexdigest()