import math
import pandas as pd
import numpy as np

class CentralTendency:
    def __init__(self):
        pass
        
    def Mean(self, values):
        summation = 0
        for x in values:
            summation  = summation + x
        mean = summation / len(values)
        return mean

    def StandardDeviation(self, values):
        
        mean = self.Mean(values)
        deviation =  0
        for x in values:
            deviation = deviation + ( (x - mean) * (x - mean) )
        standardDeviation = math.sqrt(deviation / (len(values) - 1))
        return standardDeviation

    def PearsonCorrelation(self, x, y):
        xMean = self.Mean(x)
        yMean = self.Mean(y)

        stdX = self.StandardDeviation(x)
        stdY = self.StandardDeviation(y)
        summ = 0
        for i in range(len(x)):
            summ += (x[i] - xMean) * (y[i] - yMean)

        rxy = summ / ((len(x)-1) * stdX * stdY)
        return rxy

    def MinMaxNorm(self, values):
        xMin = min(values)
        xMax = max(values)
        newValues = []
        for i in range(len(values)):
            newValues.append( (values[i] - xMin) / (xMax - xMin)) 
        
        return newValues


def main():
    data = pd.read_csv("toy-example.csv")
    heights = data['Height']
    print(heights)
    weights = data['Weight']
    calc = CentralTendency()

    stdForHeight = calc.StandardDeviation(heights)
    stdForWeight = calc.StandardDeviation(weights)

    print(stdForHeight)
    print(stdForWeight)
    print(np.std(heights, ddof=1))
    print(np.std(weights, ddof=1))

    rxy = calc.PearsonCorrelation(heights, weights)
    
    # print(data.corr(method='pearson'))
    if abs(rxy) < 0.00005:
        print("No Corelation : ", rxy)
    elif rxy > 0:
        print("Positive Correlation : ", rxy)
    elif rxy < 0:
        print("Negative Correlation : ", rxy)

    normedHeights = calc.MinMaxNorm(heights)
    normedWeights = calc.MinMaxNorm(weights)

    print(normedHeights)

    rxy = calc.PearsonCorrelation(heights, weights)

    if abs(rxy) < 0.00005:
        print("No Corelation : ", rxy)
    elif rxy > 0:
        print("Positive Correlation : ", rxy)
    elif rxy < 0:
        print("Negative Correlation : ", rxy)





if __name__ == '__main__':
    main()
