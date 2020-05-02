from functools import wraps

def bold(func):
    @wraps(func)
    def wrapper ():
        res = str(func())
        return '<b>'+ res + '</b>'
    return wrapper

def italic(func):
    @wraps(func)
    def wrapper ():
        res = str(func())
        return '<i>'+ res + '</i>'
    return wrapper


def underline(func):
    @wraps(func)
    def wrapper ():
        res = str(func())
        return '<u>'+ res + '</u>'
    return wrapper
