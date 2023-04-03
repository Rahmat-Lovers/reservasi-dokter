from functools import wraps as _wraps
from django.forms import Form as _Form
from main.exceptions import ValidationError as _ValidationError

def check_error(form: _Form, form_key: str = "payload"):
    def decorator(function):
        @_wraps(function)
        def wrapper(*args, **kwargs):
            sekeren: _Form = form(kwargs[form_key].dict())
            if not sekeren.is_valid():
                raise _ValidationError(sekeren)
            
            return function(*args, **kwargs)
        return wrapper
    
    return decorator