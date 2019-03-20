import functools
import time


def profiler(func):
    profiler.exits = 0
    profiler.enters = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # all_args = tuple(list(args) + list(kwargs))
        #
        # if all_args not in profiler.recur_args:
        #     profiler.recur_args.add(all_args)
        #     profiler.counter += 1
        # else:
        #     wrapper.calls = profiler.counter
        #     profiler.counter = 0
        #
        # wrapper.calls = profiler.counter

        profiler.enters += 1

        start_time = time.time()
        result = func(*args, **kwargs)
        finish_time = time.time()

        profiler.exits += 1

        if profiler.enters == profiler.exits:
            wrapper.calls = profiler.enters
            wrapper.last_time_taken = finish_time - start_time

            profiler.enters = 0
            profiler.exits = 0

        return result

    return wrapper


# @profiler
# def func(num):
#     if num == 0:
#         return
#
#     func(num-1)
#
# func(3)
# print(func.calls)
# # куда сохраняется calls??? где его взять-то вообще?
