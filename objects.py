from abc import ABC, abstractmethod


class InternalStates(ABC):
    @abstractmethod
    def open_state(self):
        pass

    @abstractmethod
    def close_state(self):
        pass


class DoorStates(InternalStates):
    def open_state(self):
        return "открыта"

    def close_state(self):
        return "закрыта"


class LockStates(InternalStates):
    def open_state(self):
        return "открыт"

    def close_state(self):
        return "заперт"


class Door(InternalStates):
    def __init__(self):
        self.state = door_interface.close_state()

    def open_state(self):
        self.state = door_interface.open_state()

    def close_state(self):
        self.state = door_interface.close_state()

    def switch_state(self):
        if lock.state == lock_interface.close_state():
            return f"Дверь нельзя открыть, т.к. замок всё ещё заперт!\n"
        elif lock.state == lock_interface.open_state():
            if self.state == door_interface.open_state():
                self.state = door_interface.close_state()
                return f"Дверь {self.state}.\n"
            elif self.state == door_interface.close_state():
                self.state = door_interface.open_state()
                return f"Дверь {self.state}.\n"


class Lock(InternalStates):
    def __init__(self):
        self.state = lock_interface.close_state()

    def open_state(self):
        self.state = lock_interface.open_state()

    def close_state(self):
        self.state = lock_interface.open_state()

    def switch_state(self):
        if door.state == door_interface.open_state():
            return f"Замок нельзя запереть, т.к. дверь открыта!\n"
        elif door.state == door_interface.close_state():
            if self.state == lock_interface.close_state():
                self.state = lock_interface.open_state()
                return f"Замок {self.state}.\n"
            elif self.state == lock_interface.open_state():
                self.state = lock_interface.close_state()
                return f"Замок {self.state}.\n"


door_interface, lock_interface = DoorStates(), LockStates()
door, lock = Door(), Lock()
