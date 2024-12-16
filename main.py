def log(func):
    def wrapper(a, b):
        print(f"Викликано '{func.__name__}' з a={a}, b={b}")
        result = func(a, b)
        print(f"'{func.__name__}' поверне {result}")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

result = add(3, 5)

