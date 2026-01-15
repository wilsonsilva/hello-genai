from functools import wraps


def log_function_call(func):
    """Decorator that logs function calls with their arguments."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Format arguments
        arg_strs = [repr(arg) for arg in args]
        kwarg_strs = [f"{k}: {v!r}" for k, v in kwargs.items()]
        all_args = ", ".join(arg_strs + kwarg_strs)

        print(f"[Function Call] {func.__name__}({all_args})")
        return func(*args, **kwargs)

    return wrapper
