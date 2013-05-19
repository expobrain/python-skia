# -*- coding: utf-8 -*-

import functools


def assert_not_fail(fn):

    @functools.wraps(fn)
    def wrapper(*args, **kwds):
        try:
            fn(*args, **kwds)
        except Exception as e:
            args[0].fail(e)

    return wrapper
