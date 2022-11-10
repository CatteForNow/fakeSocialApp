# Variables
friends = []
pings   = 0

# Constantes
devices = ["Computer", "Cellphone", "Tablet"]
status  = ["Online", "Idle", "Do Not Disturb", "Offline"]
sex     = ["Male", "Female"]

# Creacion de amigos
class Friends():
    def __init__(self, name: str, age: int, sex: str, hobby: str) -> None:
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

# Crear tu usuario
my_username = input("~ Username \n")
my_age =      input("\n~ Age \n")
my_sex =      input("\n~ Sex \n")
my_hobby =    input("\n~ Hobby \n")
my_status =   input("\n~ Status \n")

# Menu principal
while True:
    print(f"""
    Connected as {my_username}    Your current status is {my_status}
    Friends {Friends.show_friends()}""")
    input()