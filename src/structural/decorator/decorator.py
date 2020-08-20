import functools


def round_decimals(_func=None, *, num_decimals=3):
    """
    Decorator to round number of decimals, by default 3
    :param _func: If this is called with arguments then _func is none
    else decorator_round_decimals will be passed as _func
    :param num_decimals: num decimals to round
    :return: number rounded with num_decimals
    """
    def decorator_round_decimals(func):
        @functools.wraps(func)
        def wrapper_round_decimals(*args, **kwargs):
            return round(func(*args, **kwargs), num_decimals)

        return wrapper_round_decimals

    if _func is None:
        return decorator_round_decimals
    else:
        return decorator_round_decimals(_func)
