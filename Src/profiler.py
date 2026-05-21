import cProfile
import pstats


def profile_function(func, *args, **kwargs):

    profiler = cProfile.Profile()

    profiler.enable()

    result = func(*args, **kwargs)

    profiler.disable()

    stats = pstats.Stats(profiler)
    stats.sort_stats("cumulative")
    stats.print_stats(10)

    return result