from abc import ABC, ABCMeta, abstractmethod


'''
    OOP CLASS:
        - field
        - properties
        - methods
            - constructor
            - destructor

    OOP:
        - inc
        - poly
        - inhe

        - abstract
        - static
        - overrides
'''


# class Entity(ABC):
class Entity(metaclass=ABCMeta):
    __metaclass__ = ABCMeta

    def __init__(self, idnx):
        self._idnx = idnx  # <- instance variable (instance field)

    @abstractmethod
    def print(self):
        pass

    def __str__(self):
        return f"Entity [{self._idnx}]"


class User(Entity):

    priority = 5                        # <- object field

    def __init__(self, idnx, name):
        super(User, self).__init__(idnx)    # <- call parent constructor

        # self.__idnx = idnx              # <- instance variable (instance field)
        self.name = name

    def print(self):
        print(self)

    def __str__(self):
        s = super(User, self).__str__().replace("Entity", "User")
        return f"{s} [{self.name}] (priority:{self.priority})"


if __name__ == '__main__':
    # e = Entity(1)
    u = User(2, 'Vlad')

    # print(e)
    # print(u)
    u.print()
    # print(isinstance(u, Entity))
    # print(isinstance(list, Entity))
    # print(issubclass(User, Entity))
    # print(issubclass(list, Entity))

    # u1 = User(0, 'Vlad')
    # u2 = User(1, 'Vova')
    # print(u1)
    # print(u2)
    # u2.priority = 7     # u2->priority=7
    # print(u1)
    # print(u2)
    # User.priority = 16  # User->priority
    # print(u1)
    # print(u2)

    # u3 = User(3, 'Igor')
    # print(u3)
