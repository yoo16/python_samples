from models.Animal import Animal

def main():
    dog = Animal("dog", "ポチ", "わん！")
    cat = Animal("cat", "ミケ", "にゃー!")
    elephant = Animal("elephant", "ジャンボ", "ぱおーん!")

    dog.walk()
    dog.cry()
    cat.cry()
    cat.escape()

main()