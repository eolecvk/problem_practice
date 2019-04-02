"""
Decorators can help to check whether someone is authorized to use an endpoint in a web application.
They are extensively used in Flask web framework and Django.
Here is an example to employ decorator based authentication:
"""


from functools import wraps

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)
    return decorated