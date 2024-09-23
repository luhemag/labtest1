import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
population_data = 1000 + np.sin(np.linspace(0, 24 * np.pi, 1440)) + np.random.rand(1440)
PM = 1000 + np.sin(np.linspace(0, 24 * np.pi, 1440)) + np.random.rand(1440)

random_noise = np.random.rand(1440)
s = sum(population_data, random_noise)
print(s)


def calculateaverage():
    print(np.mean(population_data))


calculateaverage()

populationdata = np.array([10, 30, 46, 78, 36, 768, 89, 3, 55, 77, 88, 33, 55, 34])
pm = np.array([10, 20, 30, 40, 40, 50, 60, 70, 80, 90, 33, 22, 11, 33])
print(np.mean([populationdata, pm], axis=0))
