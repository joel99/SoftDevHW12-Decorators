from decorators import log_func_signature, timer

# @timer
@log_func_signature
def naive_fib(n):
    if n < 2:
        return n
    else:
        print n - 1, n - 2
        return naive_fib(n - 1) + naive_fib(n - 2)

    #return n if n < 2 else naive_fib(n - 1) + naive_fib(n - 2)
