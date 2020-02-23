
import numpy as np
import pandas as pd
import scipy.spatial as ss

def standardized_euclidean(x, y, var=1):
    """ Mahalanobis distance with diagonal varariance matrix """
    return np.sqrt(np.sum((x - y)**2 / var))



# task 1.1

mean, var = 180, 100

print("Mean, var =", mean, var)

print("# Task 1.1")
for x in [180, 190, 170, 200, 100, 100]:
    print("D_M(%d) =" % x, standardized_euclidean(x, mean, var=var))



print("# Task 1.2")
for x, y in [(140, 220), (100, 200)]:
    print("d(%d, %d) =" % (x, y), standardized_euclidean(x, y, var=var))


del mean, var

print("# Task 1.3")

mean = np.array([177, 63]).T
cov = np.array([[75, 0],[0, 37]])

print("Mean", mean)
print("Covariance", cov)

print("D_M((182,73)) =", standardized_euclidean(np.array([182, 73]).T, mean, var=np.diag(cov)))



print("# Task 1.4")

dataframe = pd.read_csv('toy-example.csv')

height = dataframe['Height'].values
weight = dataframe['Weight'].values
data = np.vstack([height, weight])

print(data)
cov = np.cov(data)

print(cov)

cov_inv = np.linalg.inv(cov)
print(cov_inv)

d = ss.distance.mahalanobis(np.array([203, 52]), np.array([165, 53]), cov_inv)
print("Mahalanobis distance between ID 75 and ID 76", d)
d = ss.distance.mahalanobis(np.array([176, 60]), np.array([177, 64]), cov_inv)
print("Mahalanobis distance between ID 86 and ID 87", d)
