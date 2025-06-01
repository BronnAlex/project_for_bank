from src.decorators import log


def test_log():
    @log(filename="mylog.txt")
    def my_functions(x, y):
        return x + y

    result = my_functions(5, 3)
    assert result == 8

    result = my_functions(9, 3)
    assert result == 12


def test_log_consol(capsys):
    @log(filename="")
    def func_1(x):
        return x + 1

    func_1(1)
    captured = capsys.readouterr()
    assert captured.out == "func_1 ok\n"


def test_exception_logging_to_console(capsys):
    @log(None)
    def func_that_raises(x):
        raise ValueError("Ошибка!")

    func_that_raises(123)

    captured = capsys.readouterr()
    assert captured.out == "func_that_raises error: Ошибка!. Inputs: (123,), {}\n"
