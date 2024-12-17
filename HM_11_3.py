import inspect


def introspection_info(obj):
    info = {}
    # Тип объекта
    info['type'] = type(obj).__name__
    # Аттрибуты обьекта(исключаем системные аттрибуты)
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    info['attributes'] = attributes
    ##print(inspect.getmembers(obj)) (Выводит все аттрибуты)
    # Методы объекта.
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    info['methods'] = methods
    ##methods = [m for m in inspect.getmembers(obj, predicate=inspect.isfunction)]
    # Модуль, к которому объект принадлежит
    info['module'] = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else None
    return info


class Inform:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        return "Urban University"

# Создаем объект
my_obj = Inform(42)

# Получаем информацию об объекте
info = introspection_info(my_obj)
print(info)
