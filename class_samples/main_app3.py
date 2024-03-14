from models.Wizard import Wizard
from models.Warrior import Warrior
from models.Monster import Monster

wizard = Wizard("アリス")
warrior = Warrior("ボブ")
monster = Monster()

wizard.attack(monster)
print(f"{wizard.name}が、{monster.name}を攻撃！")
print(f"{monster.name}のHP: {monster.hp}")

warrior.attack(monster)
print(f"{warrior.name}が、{monster.name}を攻撃！")
print(f"{monster.name}のHP: {monster.hp}")
