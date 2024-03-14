class Monster:
    name: str = ""
    hp: int = 0
    mp: int = 0
    level: int = 1
    exp: int = 0
    attackPower: int = 0
    deffencePower: int = 0

    def __init__(self):
        self.name = "スライム"
        self.hp = 5
        self.mp = 0
        self.attackPower = 2
        self.defencePower = 1

    def attack(self, person):
        damage = self.attackPower - person.defencePower
        if damage > 0:
            person.hp -= damage
