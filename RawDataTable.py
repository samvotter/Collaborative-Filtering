import Links as l
import Movies as m
import Ratings as u
import Tags as t

import copy as c


class RawDataTable:

    def __init__(self):

        self.learningRate = .0001
        self.errorX = []
        self.errorT = []
        self.errorXT = []
        self.avgError = {}
        self.avgError["x"] = []
        self.avgError["t"] = []
        self.avgError["xt"] = []

        self.movies = m.MovieTable("movies")
        self.users = u.UserTable("ratings")
        self.tags = t.TagTable("tags")
        self.links = l.LinksTable("links")
        for user in self.users.table:
            for rating in self.users.table[user].ratings:
                self.movies.table[rating].add_rating(self.users.table[user].ratings[rating])

    def thetaTx(self, thetaList, featureList):
        total = 0
        for k in range(len(featureList)):
            total += featureList[k] * thetaList[k]
        return total

    def updateX(self):

        for movie in self.movies.table:
            for user in self.movies.table[movie].ratings:
                total = 0
                OJ = self.thetaTx(self.users.table[user].thetas, self.movies.table[movie].x)
                self.errorX.append((OJ - self.movies.table[movie].ratings[user])**2)
                for feature in range(len(self.movies.table[movie].x)):
                    total += ((OJ - self.movies.table[movie].ratings[user])*self.users.table[user].thetas[feature])
                    self.movies.table[movie].new_x[feature] -= (self.learningRate * total)
        for movie in self.movies.table:
            for feature in range(len(self.movies.table[movie].x)):
                self.movies.table[movie].x[feature] = self.movies.table[movie].new_x[feature]

    def updateTheta(self):
        for user in self.users.table:
            for movie in self.users.table[user].ratings:
                total = 0
                OJ = self.thetaTx(self.users.table[user].thetas, self.movies.table[movie].x)
                for theta in range(len(self.users.table[user].thetas)):
                    total += ((OJ - self.movies.table[movie].ratings[user])*self.movies.table[movie].x[theta])
                    self.users.table[user].newTheta[theta] -= (self.learningRate * total)
        for user in self.users.table:
            for theta in range(len(self.users.table[user].thetas)):
                self.users.table[user].thetas[theta] = self.users.table[user].newTheta[theta]

    def averageList(self, list):
        total = 0
        for i in list:
            total += i
        avg = total/(len(list))
        return avg

    def computeErrors(self):
        self.avgError["x"].append(c.deepcopy(self.averageList(self.errorX)))
        self.errorX.clear()

    def writeTable(self):
        all = []
        with open("Predicted Output.txt", 'w') as ofile:
            for movie in self.movies.table:
                ratings = []
                ofile.write(str(self.movies.table[movie].title))
                ofile.write(": ")
                for user in self.users.table:
                    OJ = (int(self.thetaTx(self.users.table[user].thetas, self.movies.table[movie].x)*100))/100
                    ratings.append(OJ)
                    ofile.write("UserID: ")
                    ofile.write(self.users.table[user].userID)
                    ofile.write(": ")
                    ofile.write(str(OJ))
                    ofile.write(" ")
                all.append([self.averageList(ratings), str(self.movies.table[movie].title)])
                ofile.write("\n")
            print("Top five highest predicted movies:")
            for i in range(0, 5):
                print(i+1, end=": ")
                print(max(all))
                all.remove(max(all))




