from models.Wizard import Wizard
from models.Warrior import Warrior

wizard = Wizard("アリス")
warrior = Warrior("ボブ")

wizard.attack(warrior)

print(f"{wizard.name}が、{warrior.name}を攻撃！")
print(f"{wizard.name}のHP: {warrior.hp}")