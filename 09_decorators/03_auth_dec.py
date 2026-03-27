from functools import wraps


def requires_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Accrs denied: Admins only.")
            return None
        else:
            return func(user_role)
    return wrapper


@requires_admin
def acces_fucker(role):
    print("Access granted: Welcome Your Fuckerrr")


acces_fucker("user")
acces_fucker("admin")
