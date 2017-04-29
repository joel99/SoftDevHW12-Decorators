from decorators import log_func_signature, timer

@timer
@log_func_signature
def naive_fib(n): return n if n < 2 else naive_fib(n - 1) + naive_fib(n - 2)

def main():
    print naive_fib(0)
    print naive_fib(3)
    print naive_fib(10)

if __name__ == '__main__':
    main()
