import time

def time_elapsed(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        print(f"Elapsed: {elapsed:.1e} s")
        return result
    return wrapper

