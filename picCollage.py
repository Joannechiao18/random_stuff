import math
from numpy import mean
import numpy as np
from scipy.stats import norm

# hypothesized family size
data = np.array([6, 7, 7, 12, 13, 13, 15, 16, 10, 22])
# hypothesized confidence intervals (margin of error)
ci_low, ci_high = -0.005, 0.005
# hypothesized confidence level
cl = 0.99
# standard deviation
std = np.std(data)
# z score
z_score = norm.ppf(1 - ((1-cl)/2))
# sample size
size = math.pow(z_score, 2)*std*(1-std)/math.pow(ci_low, 2)

index = np.random.choice(len(data), size, replace=False)  # sample uniformly
mean_arr = []
for i in range(len(index)):
    mean_arr.append(data[index[i]])

print(mean(mean_arr))
