from time import time as current_time

from utils import get_args, get_kwargs

def timer(func):
    def inner(*args, **kwargs):
        start_time = current_time()
        result = func(*args, **kwargs)
        end_time = current_time()
        print 'Execution time: {0}'.format(end_time - start_time)
        return result
    return inner

def log_func_signature(func):
    def inner(*args, **kwargs):
        args_string_form = get_args(args)
        kwargs_string_form = get_kwargs(kwargs)
        if kwargs_string_form:
            delimiter = '' if not args_string_form else ', '
            print '{0}({1}{2}{3})'.format(func.func_name, args_string_form, delimiter, kwargs_string_form)
        else:
            print '{0}({1})'.format(func.func_name, args_string_form)
        return func(*args, **kwargs)
    return inner
