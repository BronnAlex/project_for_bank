from functools import wraps


def log(filename):
    """Декоратор для логирования функций и вывода результатов в консоль или файл и
    принимающий на вход необязательный аргумент filename"""

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)

            except Exception as error:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {error}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {error}. Inputs: {args}, {kwargs}")

            else:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result

        return inner

    return wrapper


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


print(my_function(123, '5'))
