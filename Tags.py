import csv


class Tag:

    def __init__(self, userID, movieID, tag, timeStamp):
        self.userID = userID
        self.movieID = movieID
        self.tag = tag
        self.timeStamp = timeStamp

    def display(self):
        print([self.userID, self.movieID, self.tag, self.timeStamp])


class TagTable:

    def __init__(self, filename):
        self.table = {}
        header = 0
        with open(filename + ".csv") as csvFile:
            rawData = csv.reader(csvFile)
            for row in rawData:
                if header == 0:
                    header += 1
                else:
                    self.table[row[0]] = Tag(row[0], row[1], row[2], row[3])
