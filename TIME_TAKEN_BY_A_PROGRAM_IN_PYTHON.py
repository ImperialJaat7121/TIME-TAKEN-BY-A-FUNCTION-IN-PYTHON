import time ## imports the time library

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()## notes the start time of the function 
        result = func(*args, **kwargs)
        end_time = time.time()## notes the end time of the function
        print(f"Function {func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper

@timer_decorator ## syntax to call the decorator function
def complex_calculation(n):
    return sum(x**2 for x in range(n))

# Test
print(complex_calculation(10000000))
