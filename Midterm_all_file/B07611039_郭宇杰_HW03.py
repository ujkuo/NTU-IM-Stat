#!/usr/bin/env python
# coding: utf-8

# # Stat HW03 by 郭宇杰, B07611039

# In[2]:


from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import scipy.stats as stats
import statsmodels.api as sm
import statsmodels.stats.api as sms
import statsmodels.formula.api as smf
import math as math


# ### 4.3
# - a

# In[3]:



### We can directly use the function in np to calculate the mean and median value instead of counting by ourself.
def mean(data):
    total = 0
    for i in range(np.size(data)):
        total += data[i]
    return total / np.size(data)

def median(data):
    data.sort()
    half = int(np.size(data)/2)
    return (data[half] + data[half - 1]) / 2

data = np.array([5.5, 7.2, 1.6, 22.0, 8.7, 2.8, 5.3, 3.4, 12.5, 18.6, 8.3, 6.6])

mean_value = np.mean(data)
median_value = np.median(data)
print("Mean: ", mean_value, "Miles")
print("Median: ", median_value, "Miles")
print("There is no Mode.")


# - b
# There is no mode indicates that there is no duplicate number in the data, and the mean value is larger than median indicates that the second half data is larger than the first half.

# ### 4.11
# - a

# In[4]:


price = np.array([10, 14, 15, 22, 30, 25])
buying_price = 12
rate = np.zeros(6)

print("The rate of return for each year:")

for i in range(int(np.size(price))):
    rate[i] = (price[i] - buying_price) / buying_price
    print("Year", i+1, ":", rate[i]*100, "%")


# - b

# In[5]:


mean_value = np.mean(rate)
median_value = np.median(rate)
print("Mean of rates of return: ", mean_value*100, "%")
print("Median of rates of return: ",median_value*100, "%")


# - c

# In[6]:


def geomean(rate):
    rate_1 = rate + 1
    geo_m = math.exp(np.log(rate_1).mean()) - 1
    return geo_m

geomean_value = geomean(rate)
print("Geometric mean of rates of return: ",geomean_value*100, "%")


# - d
# When the data is dealing with the 'growth rate or rate of change' in variable over time, the best statistic to use to describe is geometric mean. That's why we use the geometric mean here.

# ### 4.17
# Assume that the unit of speeds is kilometer per hour(km/hr).
# - a
# 

# In[7]:


data_4_17 = pd.read_excel('Xr04-17.xlsx')
mean_value = np.mean(data_4_17["Speeds"])
median_value = np.median(data_4_17["Speeds"]) 
## We can directly use the np function to find median and mean......
print("Mean Value: ", mean_value, "km/hr")
print("Median Value: ", median_value, "km/hr")


# Mean value is approximate with median value indicates that there isn't too much extreme value in the data.

# ### 4.31
# The sample b has the smallest amount of variation and the sample c has the largest one. We can observate the distribution of number in each sample to speculate the size of variation, since the sample c has the biggest and the smallest number among these 3 sample, as a result, we can indicate that the sample c has the largest amount of variation. We can use the same method to indicate the sample with the smallest amount of variation.

# ### 4.41
# Assume that the unit of distance is meter(m).
# - a
# 

# In[8]:


data_4_41 = pd.read_excel('Xr04-41.xlsx')
punter1 = data_4_41['Punter 1']
punter2 = data_4_41['Punter 2']
punter3 = data_4_41['Punter 3']

print("Variance for Punter 1 = ", np.std(punter1, ddof = 1)**2, "m")
print("Variance for Punter 2 = ", np.std(punter2, ddof = 1)**2, "m")
print("Variance for Punter 3 = ", np.std(punter3, ddof = 1)**2, "m")

print("Standard Deviation for Punter 1 = ", np.std(punter1, ddof = 1), "m")
print("Standard Deviation for Punter 2 = ", np.std(punter2, ddof = 1), "m")
print("Standard Deviation for Punter 3 = ", np.std(punter3, ddof = 1), "m") # default ddof = 0 (N-0), set ddof = 1 to adjust degree of freedom
# print(punter3.std()) # N-1

# typically we use the sample std (N-1)


# - b
# 
# Punter 3 is more consistent than the other two punters since its standard deviation is smaller than others; also, punter 1 is more distributed.

# ### 4.47
# Assume that the unit of property tax is US Dollar.
# - a

# In[9]:


data_4_47 = pd.read_excel('Xr04-47.xlsx')
data_4_47 = data_4_47['Property tax']
mu = data_4_47.mean()
std = data_4_47.std()

print("Mean = ", data_4_47.mean(), "US Dollars")
print("Standard Deviation = ", data_4_47.std(), "US Dollars")


# In[10]:


total = 0
for i in data_4_47:
    total += (i - mu)**3
    
total = total / int(len(data_4_47))    
skewness = total / std**3
print("The skewness is: ", skewness)


# According to the skewness we calculate, this data is skewed. As a result, by the chebysheff's theorem, the rule will aply that 

# In[12]:


k1 = 1
print("At least ", (1 - (1 / (k1**2))) * 100 , "% of data lie in range (", float(np.mean(data_4_47) - k1 * np.std(data_4_47, ddof = 1)), 
      ",", float(np.mean(data_4_47) + k1 * np.std(data_4_47, ddof = 1)), ") US Dollars.")

k2 = 2
print("At least ", (1 - (1 / (k2**2))) * 100 , "% of data lie in range (", float(np.mean(data_4_47) - k2 * np.std(data_4_47, ddof = 1)), 
      ",", float(np.mean(data_4_47) + k2 * np.std(data_4_47, ddof = 1)), ") US Dollars.")

k3 = 3
print("At least ", (1 - (1 / (k3**2))) * 100 , "% of data lie in range (", float(np.mean(data_4_47) - k3 * np.std(data_4_47, ddof = 1)), 
      ",", float(np.mean(data_4_47) + k3 * np.std(data_4_47, ddof = 1)), ") US Dollars.")


# ## All problems in the hw 3 is solved, and my answers are shown as above. Thank TAs for reading and checking my homework!
