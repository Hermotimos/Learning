import time


def time_function(function, print_args=True):
    """Returns function execution time

    Possible changes for different measured units:
    - for seconds:              time.time()
    - for nanoseconds:          time.perf_counter_ns()
    - for fractional seconds:   time.perf_counter

    Conversion from nanoseconds to seconds: * 0.000000001
    Conversion from scientific notation (ex. 2.14e-04) to float with precision 10: format() with {:.10f}
    """
    def wrapper(*args):
        timer_start = time.perf_counter_ns()
        function(*args)
        timer_stop = time.perf_counter_ns() - timer_start
        print('Time for {}({}): {:.10f} secs'.format(
                                                        function.__name__,
                                                        ",".join(str(a) for a in args) if print_args else '',
                                                        timer_stop * 0.000000001
                                                        )
              )
    return wrapper
