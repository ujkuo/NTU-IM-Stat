#!/usr/bin/env python
# coding: utf-8

# # Stat HW04 by 郭宇杰, B07611039from matplotlib import pyplot as plt

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


# ### 4.39

# In[13]:


data = pd.read_excel('Xr04-39.xlsx')['Prozac']
range_value = max(data) - min(data)
print("Range for Prozac cost is",range_value,"dollars per 100 pills")
print("Variance for Prozac cost is", np.std(data, ddof = 1)**2, "dollars per 100 pills")
print("Standard deviation for Prozac cost is", np.std(data, ddof = 1), "dollars per 100 pills")


# In[9]:


mu = data.mean()
std = data.std()
total = 0
for i in data:
    total += (i - mu)**3
    
total = total / int(len(data))    
skewness = total / std**3
print("The skewness is: ", skewness)


# Since the data is skewed, we can use the Chebyshev theorem, at least 75% of the Prozac price lies within 2\*std approximate equal to 10.86 dollars per 100 pills of the mean, and at least 89% of the Prozac price lies within 3\*std approximate equal to 16.29 dollars per 100 pills of the mean

# ### 4.45

# In[15]:


data = pd.read_excel('Xr04-45.xlsx')['Flight delay (minutes)']
mean = data.mean()
std = np.std(data, ddof = 1)
print("The mean value of the time is",mean,"minutes")
print("The standard deviation of the time is",std,"minutes")


# Since the distribution is approximately bell shaped, according to the empirical rule, 68% observations lies within the range $(\bar x - s, \bar x + s)$, that is (14.27, 27.84). In addition, 95% obsercations lies within the range $(\bar x - 2s, \bar x + 2s)$ and 99.7% obsercations lies within the range $(\bar x - 3s, \bar x + 3s)$, which is (-0.56,46.64) and (-7.2, 59.28) respectively.

# ### 4.61

# In[4]:


data = pd.read_excel('Xr04-61.xlsx')['X']

### Use the function written by Prof.

def percentile(data1, p):
    if type(data1) == np.ndarray:        
        alldata = data1.copy()
        data1 = data1.copy()
    else:
        alldata = data1.values.copy()
        data1 = data1.values.copy()
    alldata.sort()
    n = alldata.size
    l = (n + 1) * p / 100 - 1
    f_l = math.floor(l)
    c_l = math.ceil(l)
    percentile_v = alldata[f_l] + (alldata[c_l] - alldata[f_l]) * (l - f_l)
    return percentile_v

L_25 = percentile(data, 25)
L_50 = percentile(data, 50)
L_75 = percentile(data, 75)
print("The first quartile for the given data is",L_25)
print("The second quartile for the given data is",L_50)
print("The third quartile for the given data is",L_75)


# ### 4.63

# In[18]:


print("The interquartile range for the given data is", L_75 - L_25)


# ### 4.69
# Assume that the unit of the given data is dollar.

# In[29]:


data = pd.read_excel('Xr04-69.xlsx')
# print(data['Cats'])

L_25_dog = percentile(data['Dogs'], 25)
L_50_dog = percentile(data['Dogs'], 50)
L_75_dog = percentile(data['Dogs'], 75)

L_25_cat = percentile(data.iloc[1:55, 1], 25)
L_50_cat = percentile(data.iloc[1:55, 1], 50)
L_75_cat = percentile(data.iloc[1:55, 1], 75)

print("The cost of dog owners :")
print("The first quartile for the cost of dog owners is", L_25_dog, "dollars")
print("The second quartile for the cost of dog owners is", L_50_dog, "dollars")
print("The third quartile for the cost of dog owners is", L_75_dog, "dollars")
print("The interquartile range for the cost of dog owners is", L_75_dog - L_25_dog, "dollars")
print("The midhinge for the cost of dog owners is", (L_25_dog + L_75_dog) / 2,"dollars")
print("\n")

print("The cost of cat owners :")
print("The first quartile for the cost of cat owners is", L_25_cat, "dollars")
print("The second quartile for the cost of cat owners is", L_50_cat, "dollars")
print("The third quartile for the cost of cat owners is", L_75_cat, "dollars")
print("The interquartile range for the cost of cat owners is", L_75_cat - L_25_cat, "dollars")
print("The midhinge for the cost of cat owners is", (L_25_cat + L_75_cat) / 2,"dollars")


# Since the IQR of the cost of cat owners is smaller that the IQR of the cost of dog owners, we can say thay the data of the cost of cat owner is more concerntrated. And based on the each quartile for the cost, we can find that dog owners spend more money that cat owners.

# ### 4.73
# Assume that the unit of the given data is minute.

# In[8]:


data = pd.read_excel('Xr04-73.xlsx')

firstQ_private = percentile(data['Private'], 25)
secondQ_private = percentile(data['Private'], 50)
thirdQ_private = percentile(data['Private'], 75)

firstQ_public = percentile(data.iloc[1:103, 1], 25)
secondQ_public = percentile(data.iloc[1:103, 1], 50)
thirdQ_public = percentile(data.iloc[1:103, 1], 75)

print("The amount of time taken for private course:")
print("The first quartile for the amount of time taken for private course is", firstQ_private, "minutes.")
print("The second quartile for the amount of time taken for private course is", secondQ_private, "minutes.")
print("The third quartile for the amount of time taken for private course is", thirdQ_private, "minutes.")
print("The interquartile range for the amount of time taken for private course is", thirdQ_private - firstQ_private, "minutes.")
print("\n")

print("The amount of time taken for public course:")
print("The first quartile for the amount of time taken for public course is", firstQ_public, "minutes.")
print("The second quartile for the amount of time taken for public course is", secondQ_public, "minutes.")
print("The third quartile for the amount of time taken for public course is", thirdQ_public, "minutes.")
print("The interquartile range for the amount of time taken for public course is", thirdQ_public - firstQ_public, "minutes.")
print("\n")


# Since the second quartile for the amount of time taken for private course is less than public's one, we can say that the amount of time taken for public courses is larger than the private courses.

# ### 4.91
# Assume that the unit of price of oil is dollar, and the unit of oil wells is thousand wells.

# In[14]:


data = pd.read_excel('Xr04-91.xlsx')

covariance = np.cov(data[['Price of Oil', 'Oil Wells']].values, rowvar = False)
correlation = np.corrcoef(data[['Price of Oil', 'Oil Wells']].values, rowvar = False)

print("The covariance matrix is \n", covariance)
print("The correlation matrix is \n", correlation)
print("\n")

print("The covariance of price of oil and oil wells is", covariance[0][1])
print("The coefficient of correlation of price of oil and oil wells is", correlation[0][1])


# The covariance of given data indicate that price of oil and oil wells are positively related, and the coefficient of correlation of given data shows that there is a very week positive linear relationship between price of oil and oil wells.

# ### 4.99
# Assume that the unit of age is year, and the unit of carbon monoxide is ppm.

# In[15]:


data = pd.read_excel('Xr04-99.xlsx')

covariance = np.cov(data[['Age', 'Carbon monoxide']].values, rowvar = False)
correlation = np.corrcoef(data[['Age', 'Carbon monoxide']].values, rowvar = False)

print("The covariance matrix is \n", covariance)
print("The correlation matrix is \n", correlation)
print("\n")

print("The covariance of age and carbon monoxide is", covariance[0][1])
print("The coefficient of correlation of age and carbon monoxide is", correlation[0][1])


# The covariance of given data indicate that age and carbon monoxide are positively related, and the coefficient of correlation of given data shows that there is a very strong positive linear relationship between age and carbon monoxide.

# ### 6.7
# - a
# $P(Adams loses) = 1 - P(Adams wins) = 1 - 0.42 = 0.58$
# - b
# $P(Brown wins or Dalton wins) = P(Brown wins) + P(Dalton wins) = 0.09 + 0.22 = 0.31$
# - c 
# $P(Adams, Brown or Collins wins) = P(Adams wins) + P(Brown wins) + P(Collins wins) = 0.42 + 0.09 + 0.27 = 0.78$

# ### 6.11
# - a
# The sample space for this experiment is $S = \{cash, credit card, debit card \} $
# - b 
# $P(cash) = 0.3, P(credit card) = 0.6, P(debit card) = 0.1$
# - c
# Subjective approach or relative frequency approach, since the statement doesn't tell us how it estimates th proprietor.

# ## All problems in the hw 4 is solved, and my answers are shown as above. Thank TAs for reading and checking my homework!
# ps. If my homework page is still too dark to read, please inform me or check from my github repository: https://github.com/ujkuo/NTU-IM-Stat
