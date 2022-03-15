#!/usr/bin/env python3
""" uses"""

from functools import wraps
import redis
import requests
from typing import Callable

r = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """ count requests """
    @wraps(method)
    def wrapper(url):
        """ wrapper method """
        r.incr(f"count:{url}")
        cache_html = r.get(f"cached:{url}")
        if cache_html:
            return cache_html.decode("utf-8")
        
        html = method(url)
        r.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """ uses the request """
    req = requests.get(url)
    return req.text
