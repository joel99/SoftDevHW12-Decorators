from flask import Blueprint, render_template

from lib.decorators import log_func_signature, timer
from lib.fib import get_fib_sequence

math_views = Blueprint('math_views', __name__)

@math_views.route('/fib')
@math_views.route('/fib/<n>')
@timer
@log_func_signature
def fib_time(n=10):
    if isinstance(n, int) or ((n, str) and n.isdigit()):
        n = int(n)
        return render_template('fib.html', fib_sequence=get_fib_sequence(n - 1))
    else:
        return render_template('404.html')
