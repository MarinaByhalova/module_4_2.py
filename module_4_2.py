def test_function():
    def inner_function():
        print(f"Я в области видимости функции test_function")

    inner_function()


inner_function() #ошибка