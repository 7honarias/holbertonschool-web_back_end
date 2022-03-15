#!/usr/bin/env python3
"""doc """
from tkinter import W
from typing import Callable, Optional
from functools import wraps
import redis
import uuid

def count_calls(method: Callable) -> Callable:
    """Counts the number of calls"""
    key = method.__qualname__

    @wraps(method)
    def wrapped(self, *args, **kwargs):
        """ get data from cache """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapped


def call_history(method: Callable) -> Callable:
    """" get data from cache """
    @wraps(method)
    def wrapped(self, *args, **kwargs):
        outputs = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":inputs", str(args))
        self._redis.rpush(method.__qualname__ + ":outputs", outputs)

        return outputs
    return wrapped


def replay(fn: Callable):
    """Display the history of calls of a particular function"""
    r = redis.Redis()
    f_name = fn.__qualname__
    n_calls = r.get(f_name)
    try:
        n_calls = n_calls.decode('utf-8')
    except Exception:
        n_calls = 0
    print(f'{f_name} was called {n_calls} times:')

    ins = r.lrange(f_name + ":inputs", 0, -1)
    outs = r.lrange(f_name + ":outputs", 0, -1)

    for i, o in zip(ins, outs):
        try:
            i = i.decode('utf-8')
        except Exception:
            i = ""
        try:
            o = o.decode('utf-8')
        except Exception:
            o = ""

        print(f'{f_name}(*{i}) -> {o}')


class Cache:
    """ class for storing"""
    def __init__(self):
        """ initialize """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data):
        """ store data in cache """
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """ get data from cache"""
        result = self._redis.get(key)
        if fn is not None:
            result = fn(result)
        return result
    
    def get_str(self, key: str) -> str:
        """ Parameterizes a value from redis to str """
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """ Parameterizes a value from redis to int """
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except Exception:
            value = 0
        return value
