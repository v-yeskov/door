from objects import *
from input_listener import *


user_manual = f"Эта программа представляет собой симулятор двери с замком.\n" \
              f"Вы можете взаимодействовать с дверью командами 'Открыть' и 'Закрыть',\n" \
              f"а так же с замком командами 'Отпереть' и 'Запереть'.\n" \
              f"По умолчанию дверь и замок находятся в закрытом состоянии.\n" \
              f"Для выхода из программы введите команду 'Выход' в любой момент.\n"
print(user_manual)

# инициализируем основной цикл программы
while True:
    try:
        action = listener.listen_input()
    except ExceptionUserInputError as e:
        print(e)
    else:
        if action == "выход":
            print("Выход из программы.")
            break
        elif action == "открыть":
            if door.state == door_interface.open_state():
                print("Дверь уже находится в открытом состоянии!\n")
            else:
                print(door.switch_state())
        elif action == "закрыть":
            if door.state == door_interface.close_state():
                print('Дверь уже находится в закрытом состоянии!\n')
            else:
                print(door.switch_state())
        elif action == "отпереть":
            if lock.state == lock_interface.open_state():
                print("Замок уже находится в открытом состоянии!\n")
            else:
                print(lock.switch_state())
        elif action == "запереть":
            if lock.state == lock_interface.close_state():
                print("Замок уже находится в запертом состоянии!\n")
            else:
                print(lock.switch_state())
