from matplotlib import pyplot
import numpy


numList = numpy.random.randint(200, size = 20)

print("The list of numbers we generates is: ", numList)



screen = pyplot.figure(figsize =(12,8))

pyplot.hist(numList)

pyplot.hist(numList,50)

pyplot.hist(numList, bins =[20,40,60,80,100,120,140,160,180,200])

pyplot.title("OMG AMAZING CHEESEBALLS HISTOGRAM")

pyplot.show()
