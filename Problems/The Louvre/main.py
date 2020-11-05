class Painting:
    museum = "Louvre"

    def __init__(self, title, painter, year):
        self.title = title
        self.painter = painter
        self.year = year

    def get_text(self):
        return f'"{self.title}" by {self.painter} ({self.year}) hangs in the {Painting.museum}.'


info = []

while len(info) < 3:
    info.append(input())

painting = Painting(info[0], info[1], info[2])
print(painting.get_text())
