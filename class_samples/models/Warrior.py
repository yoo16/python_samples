from models.Person import Person

class Warrior(Person):
    def __init__(self, name):
        super().__init__(name)
        self.job = "Warrior"
        self.hp = 50
        self.mp = 0
        self.attackPower = 7
        self.defencePower = 3