def start_and_end(func):
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("End")
        return result

    return wrapper


@start_and_end
def add_5(x):
    return x + 5


result = add_5(12)
print(result)
