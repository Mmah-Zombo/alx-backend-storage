import requests
import time
import functools

CACHE_EXPIRATION = 10  # Cache expiration time in seconds

def track_url_access_count(func):
    access_count = {}

    @functools.wraps(func)
    def wrapper(url):
        access_count.setdefault(url, 0)
        access_count[url] += 1
        result = func(url)
        return result

    return wrapper

@track_url_access_count
@functools.lru_cache(maxsize=None, typed=False, ttl=CACHE_EXPIRATION)
def get_page(url):
    response = requests.get(url)
    return response.text
