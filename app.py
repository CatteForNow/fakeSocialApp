# Librerias
import random
from random import randint, choice

# Variables
friends = []
pings   = 0

# Constantes
sex     = ["Male", "Female"]
status  = ["Online", "Idle", "Do Not Disturb", "Offline"]
devices = ["Computer", "Cellphone", "Tablet"]

# Creacion de amigos
class Friends():
    def __init__(self, name: str, age: int, sex, hobby: str) -> None:
        self.name = name
        self.age = age
        self.sex = sex
        self.hobby = hobby

    # Funcion que muestra la cantidad de amigos
    def show_friends() -> int:
        counter = 0
        for n in friends:
            counter += 1
        return counter

    def create_random_friend():
        return Friends("catty", randint(14, 20), random.choice(sex), "asd")

    def __str__(self) -> str:
        return str(self.__dict__)

print(Friends.create_random_friend())

# Crear tu usuario
class User:
    def __init__(self, name: str, age: int, sex: list[str], hobby, status, device) -> None:
        self.name = name
        self.age = age
        self.sex = sex
        self.hobby = hobby
        self.status = status
        self.device = device

    def __str__(self) -> str:
        return str(self.__dict__)

my_user = User("Catte", 15, sex[0], "Listen to music", status[0], devices[0])
print(my_user)

# Menu principal
while True:
    print(f"""
    Connected as {my_user.name}    Your current status is {my_user.status}
    Friends {Friends.show_friends()}""")
    input()
