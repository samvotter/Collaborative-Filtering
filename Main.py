import matplotlib.pyplot as plt
import RawDataTable as RDT


table = RDT.RawDataTable()
numberOfIterations = 30
for i in range(0, numberOfIterations):
    table.updateX()
    table.updateTheta()
    table.computeErrors()
    print("I have completed", i+1, "cycles through the data.")
    print("Average Error rate:", table.avgError["x"][i])


plt.plot(table.avgError["x"])
plt.title("Average Error Rate for Features")
plt.ylabel("Error Magnitude")
plt.xlabel("Number of Iterations.")
plt.show()

plt.plot(table.avgError["t"])
plt.title("Average Error Rate for User Preferences.")
plt.ylabel("Error Magnitude")
plt.xlabel("Number of Iterations.")
plt.show()
