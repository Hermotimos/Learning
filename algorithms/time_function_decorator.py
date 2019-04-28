import time


def time_function(function):
    """Returns function execution time

    Possible changes for different measured units:
    - for seconds:              time.time()
    - for nanoseconds:          time.perf_counter_ns()
    - for fractional seconds:   time.perf_counter

    Conversion from nanoseconds to seconds: * 0.000000001
    """
    def wrapper(*args):
        timer_start = time.perf_counter_ns()
        function(*args)
        timer_stop = time.perf_counter_ns() - timer_start
        print('Time for {:25}: {} secs'.format(function.__name__, round(timer_stop * 0.000000001, 7)))
    return wrapper
