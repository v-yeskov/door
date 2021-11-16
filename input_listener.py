class ExceptionUserInputError(Exception):
    """Класс исключения при вводе некорректных данных"""
    def __init__(self, *args):
        super().__init__(self, *args)
        self.message = args[0] if args else None

    def __str__(self):
        return f"Ошибка: {self.message}\n"


class InputListener:
    """Класс-слушатель пользовательского ввода"""

    @staticmethod
    def listen_input():
        user_input = input("Введите действие:\n")
        user_input = user_input.strip().lower()
        analyzer.analyze_user_input(user_input)
        return user_input


class InputAnalyzer:
    """Класс-анализатор пользовательского ввода"""

    @staticmethod
    def analyze_user_input(u_input):
        if u_input not in user_actions:
            raise ExceptionUserInputError("такой команды не существует!")


user_actions = ["открыть",
                "закрыть",
                "отпереть",
                "запереть",
                "выход",
                ]
listener = InputListener()
analyzer = InputAnalyzer()
