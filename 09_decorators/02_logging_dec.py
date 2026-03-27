from functools import wraps


def log_activity(func):
    @wraps(func)
    def wrapper(*agrs, **kwargs):
        print(f"Calling: {func.__name__}")
        result = func(*agrs, **kwargs)
        print(f"Finished: {func.__name__}")
        return result
    return wrapper


@log_activity
def brew_chai(type):
    print(f"Brewing {type} chai...")


brew_chai("masala")
