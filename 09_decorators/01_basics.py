from functools import wraps

def my_dec(func):
    @wraps(func)
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper


@my_dec
def greet():
    print("Hello, Bhai kya haal mere ladallle")


greet()
print(greet.__name__)
