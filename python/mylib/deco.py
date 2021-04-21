# write a simple decorator to check the time it tooks to run different functions
import datetime # it was inside the second def

def timer_decorator(func):
    print("Decorator init")
    """
    To use this, just add @timer_decorator before your function
    """
    def timer_wrapper(*args, **kwargs):
        print("Decoractor before start")
        before = datetime.datetime.now()
        result = func(*args, **kwargs)
        after = datetime.datetime.now()
        print(f"Elasped time = {after - before}")
        return result
