import matplotlib.pyplot as plt
import RawDataTable as RDT
import time


table = RDT.RawDataTable()
numberOfIterations = 60
start = time.time()
for i in range(0, numberOfIterations):
    table.updateX()
    table.updateTheta()
    table.computeErrors()
    print("I have completed", i+1, "cycles through the data.")
    print("Average Error Rate:", table.avgError["x"][i])
end = time.time()

duration = end - start
print("This took", int(duration), "seconds.")

plt.plot(table.avgError["x"])
plt.title("Average Error Rate")
plt.ylabel("Error Magnitude")
plt.xlabel("Number of Iterations.")
plt.show()

print("\nCreating the output table - this takes about as long as the algorithm.")
table.writeTable()
