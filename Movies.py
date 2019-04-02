import csv
import random
import copy


class Movie:

    def __init__(self, movieID, title, genre):
        self.movieID = movieID
        self.title = title
        self.genre = self.dissect(genre)
        self.ratings = {}
        self.average = 0

        self.x = []
        for i in range(0, 10):
            self.x.append(int((random.randint(1, 2) / random.randint(10, 100))*10000)/10000)
        self.new_x = copy.deepcopy(self.x)

    def dissect(self, genre):
        genres = []
        buffer = ""
        for letter in genre:
            if letter != "|":
                buffer += letter
            else:
                genres.append(buffer)
                buffer = ""
        return genres

    def displayRatings(self):
        print([self.movieID, self.title, self.genre])

    def add_rating(self, rating):
        self.ratings[rating.userID] = float(rating.rating)

    def calc_average(self):
        for rating in self.ratings:
            self.average += self.ratings[rating]
        if len(self.ratings) > 0:
            self.average /= len(self.ratings)


class MovieTable:

    def __init__(self, filename):
        self.table = {}
        header = 0
        with open(filename + ".csv") as csvFile:
            rawData = csv.reader(csvFile)
            for row in rawData:
                if header == 0:
                    header += 1
                else:
                    self.table[row[0]] = Movie(row[0], row[1], row[2])

    def displayRatings(self):
        for movie in self.table:
            if len(self.table[movie].ratings) > 0:
                print(self.table[movie].title, self.table[movie].ratings)
            else:
                print(self.table[movie].title, "has no ratings")

    def displayFeatures(self):
        for movie in self.table:
            print(self.table[movie].title, self.table[movie].x)
