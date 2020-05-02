from functools import wraps

class MyCustomException(Exception):
    """My custom exception message"""
    pass

def raises(error_name):
    def real_deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func()
            except:
                return error_name.__name__
        return wrapper
    return real_deco

@raises(MyCustomException)
def return_str():
    return "test"+ 7
return_str("Hello world") # Ошибка FileNotFoundError
