import csv


class Link:

    def __init__(self, ID, imdb, tmdb):
        self.ID = ID
        self.imdb = imdb
        self.tmdb = tmdb

    def display(self):
        print([self.ID, self.imdb, self.tmdb])


class LinksTable:

    def __init__(self, filename):
        self.table = {}
        header = 0
        with open(filename+".csv") as csvFile:
            rawData = csv.reader(csvFile)
            for row in rawData:
                if header == 0:
                    header += 1
                else:
                    self.table[row[0]] = Link(row[0], row[1], row[2])
