# Напишите декоратор log
# , который будет автоматически логировать начало и конец выполнения функции, а также ее результаты или возникшие ошибки.
# Декоратор должен принимать необязательный аргумент filename
# который определяет, куда будут записываться логи (в файл или в консоль):
# Если filename задан, логи записываются в указанный файл.
# Если filename не задан, логи выводятся в консоль.
# Логирование должно включать:
# Имя функции и результат выполнения при успешной операции.
# Имя функции, тип возникшей ошибки и входные параметры, если выполнение функции привело к ошибке.
from logging import exception


def log(filename=""):
    def my_decorator(func):
        def wrapper(*args):

            try:
                result = func(*args)
                if filename != "mylog.txt":
                    print(f"{func.__name__} ok")
                elif filename == "mylog.txt":
                    with open(filename, "w", encoding='utf-8') as file:
                        file.write(f"{func.__name__} ok")
                return result
            except TypeError:
                error = f'необходимо числовое значение, а не строковое'
                if filename == "mylog.txt":
                    with open(filename, "w", encoding='utf-8') as file:
                        file.write(f"{func.__name__} error: {error}. Inputs: {args}")
                else:
                    print(f"{func.__name__} error: {error}. Inputs: {args}")
            return TypeError("Введите числовое значение")

        return wrapper

    return my_decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


print(my_function(5, 2))
