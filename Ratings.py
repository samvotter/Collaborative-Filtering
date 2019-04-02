import csv
import random
import copy


class Rating:

    def __init__(self, userID, movieID, rating, timeStamp):
        self.userID = userID
        self.movieID = movieID
        self.rating = rating
        self.timeStamp = timeStamp


class User:

    def __init__(self, userID):
        self.userID = userID
        self.ratings = {}

        self.thetas = []
        for i in range(10):
            self.thetas.append(int((random.randint(1, 2) / random.randint(10, 100))*10000)/10000)
        self.newTheta = copy.deepcopy(self.thetas)

    def addRating(self, item):
        self.ratings[item.movieID] = item


class UserTable:

    def __init__(self, filename):
        self.table = {}
        header = 0
        with open(filename+".csv") as csvFile:
            rawData = csv.reader(csvFile)
            for row in rawData:
                if header == 0:
                    header += 1
                else:
                    if row[0] in self.table:
                        self.table[row[0]].addRating(Rating(row[0], row[1], row[2], row[3]))
                    else:
                        self.table[row[0]] = User(row[0])
                        self.table[row[0]].addRating(Rating(row[0], row[1], row[2], row[3]))

