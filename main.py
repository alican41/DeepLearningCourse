def my_decorator(func):
    def wrapper():
        print("Wrapper function executed")
        func()
        print("Wrapper function executed")
        
    return wrapper


@my_decorator
def hello_world():
    print("Hello, World!")

hello_world()