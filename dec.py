from time import time as current_time

def metaDecorator(function):
    def log_function(*args, **kwargs):
        print function.func_name + '(' + str(*args) + str(','.join([str(i) for i in kwargs.values()])) + ')'
        # print '{0}({1}{2})'.format(function.func_name, *args, ','.join(**kwargs.value))
        return function(*args, **kwargs)
    return log_function
"""
def timer(f):
    def inner(*args, **kwargs):
        start_time = current_time()
        f(*args, **kwargs)
        end_time = current_time()
        print end_time - start_time
    return inner
"""
@metaDecorator
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

fib(5)

def timer(f):
    def inner(*arg):
        start_time = current_time()
        f(*arg)
        end_time = current_time()
        print end_time - start_time
        return end_time - start_time
    return inner

@timer
def slowFib(n):
    if n < 2:
        return n
    return slowFib(n - 1) + slowFib(n - 2)

slowFib(30)
