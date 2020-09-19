class Painting:
    museum = "Louvre"

    def __init__(self, artist, title, year):
        self.artist = artist
        self.title = title
        self.year = year
        print(f'"{self.title}" by {self.artist} ({self.year}) hangs in the {Painting.museum}.')


data = []

for _ in range(3):
    data.append(input())

paint = Painting(data[1], data[0], data[2])
