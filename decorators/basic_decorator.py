def increments(f):
    def wrapped_f(*args, **kwargs):
        return int(f(*args, **kwargs)) + 1
    return wrapped_f

@increments
def plus(a, b):
    return a + b

print(plus(4, 6))  # 11