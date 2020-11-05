class Angel:
    color = "white"
    feature = "wings"
    home = "Heaven"


class Demon:
    color = "red"
    feature = "horns"
    home = "Hell"


nice_pair = [Angel(), Demon()]

for entity in nice_pair:
    print(entity.color)
    print(entity.feature)
    print(entity.home)
