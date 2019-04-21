import time


def time_function(function):
    def wrapper(*args):
        timer_start = time.time()
        function(*args)
        timer_stop = time.time() - timer_start
        print('Time elapsed for {}({}): {}'.format(function.__name__, ",".join(str(a) for a in args), timer_stop))
    return wrapper
