class Person:
    name: str = ""
    job: str = ""
    hp: int = 0
    mp: int = 0
    level: int = 1
    exp: int = 0
    attackPower: int = 0
    deffencePower: int = 0

    def __init__(self, name):
        self.name = name

    def walk(self, direction: str):
        message = f"{self.name} move to {direction}"
        print(message)

    def talk(self, person, message):
        message = f"{person.name}！{message}"
        print(message)

    def attack(self, person):
        damage = self.attackPower - person.defencePower
        if damage > 0:
            person.hp -= damage
