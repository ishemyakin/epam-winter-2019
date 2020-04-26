from functools import wraps

def bold(func):
    @wraps(func)
    def wrapper (*args, **kwargs):
        # res = '<b>'+ some_text + '</b>'
        return '<b>' + func() + '</b>'
    return wrapper

def italic(func):
    @wraps(func)
    def wrapper (*args, **kwargs):
        # res ='<i>'+ some_text + '</i>'
        return '<i>' + func() + '</i>'
    return wrapper


def underline(func):
    @wraps(func)
    def wrapper (*args, **kwargs):
        # res ='<i>'+ some_text + '</i>'
        return '<u>' + func() + '</u>'
    return wrapper


@bold
@italic
@underline
def html_test(text):
    print(f"{text}")

text = "My shiny string"


html_test("My shiny string")
