from functools import wraps


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            log_message = f"Начало выполнения функции '{func.__name__}' с аргументами {args} и {kwargs}\n"

            try:

                result = func(*args, **kwargs)

                log_message += f"Функция '{func.__name__}' успешно завершена с результатом: {result}\n"
            except Exception as e:

                log_message += f"Функция '{func.__name__}' завершилась с ошибкой: {type(e).__name__}, {e}\n"

                result = None


            if filename:
                with open(filename, 'a', encoding="utf--8") as file:
                    file.write(log_message)
            else:
                print(log_message)

            return result

        return wrapper

    return decorator


# Пример использования декоратора
@log("mylog.txt")
def my_function(x, y):
    return x / y


# Тестирование функции
my_function(10, 2)  # Успешный вызов
my_function(10, 0)  # Вызов с ошибкой
