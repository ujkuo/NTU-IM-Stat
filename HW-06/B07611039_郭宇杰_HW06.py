#!/usr/bin/env python
# coding: utf-8

# # Stat HW06 by 郭宇杰, B07611039

# ### 7.13
# - a
# 
# $P(A \ graduate \ is \ offered \ fewer \ than \ two \ jobs) = 0.05 + 0.43 = 0.48$
# 
# - b
# 
# $P(A \ graduate \ is \ offered \ more \ than \ one \ job) = 0.31 + 0.21 = 0.52$

# ### 7.27
# - a
# 
# $P(X \geq 20) = 0.08 + 0.05 + 0.04 + 0.04 + 0.03 + 0.03 + 0.01 = 0.28$
# 
# - b
# 
# $P(X = 60) = 0$
# 
# - c
# 
# $P(X > 50) = 0.03 + 0.01 = 0.04$
# 
# - d
# 
# $P(X > 100) = 0$

# ### 7.35
# 
# $\mu = 0 \times 0.01 + 1 \times 0.20 + 2 \times 0.25 + 3 \times 0.25 + 4 \times 0.2 = 2.25$
# 
# $V(x) = \sigma ^2 = \sum (x - \mu )^2 P(x) = 1.5875$
# 
# $\sigma = \sqrt{\sigma ^2} = 1.25996$

# ### 7.55
# Denote the joint prabability distribution of X and Y is $P(X,Y)$.
# 
# $P(0,1) = 0.04$
# $P(0,2) = 0.08$
# $P(0,3) = 0.08$
# $P(1,1) = 0.16$
# $P(1,2) = 0.32$
# $P(1,3) = 0.32$

# ### 7.59
# 
# - a
# 
# $P(X=0, Y=2) = 0.06$
# 
# - b
# 
# $P(X=2, Y=0) = 0$
# 
# - c
# 
# $P(X \leq 1, Y \leq 1) = P(X=0, Y=0) + P(X=0, Y=1) + P(X=1, Y=0) + P(X=1, Y=1) = 0.67$

# ### 7.79
# - a

# In[1]:


from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import seaborn as sns
import pandas as pd
import numpy as np
import scipy.stats as stats
import statsmodels.api as sm
import statsmodels.stats.api as sms
import statsmodels.formula.api as smf
import math as math
data = pd.read_excel('Xr07-NYSE.xlsx')


# In[32]:


weight = np.array([0.25, 0.25, 0.25, 0.25])
mean = np.array([data['GE'].mean(), data['JNJ'].mean(), data['MCD'].mean(), data['MRK'].mean()])
std = np.array([data['GE'].std(), data['JNJ'].std(), data['MCD'].std(), data['MRK'].std()])

data_to_array = np.array(data[['GE', 'JNJ', 'MCD', 'MRK']]).T # transpose is necessary
covariance = np.cov(data_to_array)
# print(covariance)

Weighted_Mean = 0
Weighted_Covariance = 0
for i in range(0,4):
    Weighted_Mean += weight[i] * mean[i]
    for j in range(0,4):
        if i != j:
            Weighted_Covariance += weight[i]*weight[j]*covariance[i][j]
        else:
            Weighted_Covariance += weight[i] * weight[i] * covariance[i][i]
print("Mean =", Weighted_Mean)
print("Standard deviation =", math.sqrt(Weighted_Covariance))


# - b

# In[30]:


weight = np.array([0.05, 0.30, 0.40, 0.25])
mean = np.array([data['GE'].mean(), data['JNJ'].mean(), data['MCD'].mean(), data['MRK'].mean()])
std = np.array([data['GE'].std(), data['JNJ'].std(), data['MCD'].std(), data['MRK'].std()])

data_to_array = np.array(data[['GE', 'JNJ', 'MCD', 'MRK']]).T # transpose is necessary
covariance = np.cov(data_to_array)

Weighted_Mean = 0
Weighted_Covariance = 0
for i in range(0,4):
    Weighted_Mean += weight[i] * mean[i]
    for j in range(0,4):
        if i != j:
            Weighted_Covariance += weight[i]*weight[j]*covariance[i][j]
        else:
            Weighted_Covariance += weight[i] * weight[i] * covariance[i][i]
print("Mean =", Weighted_Mean)
print("Standard deviation =", math.sqrt(Weighted_Covariance))


# - c

# In[31]:


weight = np.array([0.10, 0.50, 0.30, 0.10])
mean = np.array([data['GE'].mean(), data['JNJ'].mean(), data['MCD'].mean(), data['MRK'].mean()])
std = np.array([data['GE'].std(), data['JNJ'].std(), data['MCD'].std(), data['MRK'].std()])

data_to_array = np.array(data[['GE', 'JNJ', 'MCD', 'MRK']]).T # transpose is necessary
covariance = np.cov(data_to_array)

Weighted_Mean = 0
Weighted_Covariance = 0
for i in range(0,4):
    Weighted_Mean += weight[i] * mean[i]
    for j in range(0,4):
        if i != j:
            Weighted_Covariance += weight[i]*weight[j]*covariance[i][j]
        else:
            Weighted_Covariance += weight[i] * weight[i] * covariance[i][i]
print("Mean =", Weighted_Mean)
print("Standard deviation =", math.sqrt(Weighted_Covariance))


# - d
# 
# The gambler investor would choose the portfolio c since it yeilds the highest expected return.
# 
# - e
# 
# The risk-averse investor would choose the portfolio b since it yeilds the lowest standard deviation.

# ### 7.89
# 
# - a

# In[35]:


data = pd.read_excel('Xr07-TSE.xlsx')
weight = np.array([0.25, 0.25, 0.25, 0.25])
mean = np.array([data['BMO'].mean(), data['MG'].mean(), data['POW'].mean(), data['RCL.B'].mean()])
std = np.array([data['BMO'].std(), data['MG'].std(), data['POW'].std(), data['RCL.B'].std()])

data_to_transpose_array = np.array(data[['BMO', 'MG', 'POW', 'RCL.B']]).T
covariance = np.cov(data_to_transpose_array)

Weighted_Mean = 0
Weighted_Covariance = 0
for i in range(0,4):
    Weighted_Mean += weight[i] * mean[i]
    for j in range(0,4):
        if i != j:
            Weighted_Covariance += weight[i]*weight[j]*covariance[i][j]
        else:
            Weighted_Covariance += weight[i] * weight[i] * covariance[i][i]
print("Mean =", Weighted_Mean)
print("Standard deviation =", math.sqrt(Weighted_Covariance))


# - b

# In[36]:


weight = np.array([0.20, 0.60, 0.10, 0.10])
mean = np.array([data['BMO'].mean(), data['MG'].mean(), data['POW'].mean(), data['RCL.B'].mean()])
std = np.array([data['BMO'].std(), data['MG'].std(), data['POW'].std(), data['RCL.B'].std()])

data_to_transpose_array = np.array(data[['BMO', 'MG', 'POW', 'RCL.B']]).T
covariance = np.cov(data_to_transpose_array)

Weighted_Mean = 0
Weighted_Covariance = 0
for i in range(0,4):
    Weighted_Mean += weight[i] * mean[i]
    for j in range(0,4):
        if i != j:
            Weighted_Covariance += weight[i]*weight[j]*covariance[i][j]
        else:
            Weighted_Covariance += weight[i] * weight[i] * covariance[i][i]
print("Mean =", Weighted_Mean)
print("Standard deviation =", math.sqrt(Weighted_Covariance))


# - c

# In[37]:


weight = np.array([0.10, 0.20, 0.30, 0.40])
mean = np.array([data['BMO'].mean(), data['MG'].mean(), data['POW'].mean(), data['RCL.B'].mean()])
std = np.array([data['BMO'].std(), data['MG'].std(), data['POW'].std(), data['RCL.B'].std()])

data_to_transpose_array = np.array(data[['BMO', 'MG', 'POW', 'RCL.B']]).T
covariance = np.cov(data_to_transpose_array)

Weighted_Mean = 0
Weighted_Covariance = 0
for i in range(0,4):
    Weighted_Mean += weight[i] * mean[i]
    for j in range(0,4):
        if i != j:
            Weighted_Covariance += weight[i]*weight[j]*covariance[i][j]
        else:
            Weighted_Covariance += weight[i] * weight[i] * covariance[i][i]
print("Mean =", Weighted_Mean)
print("Standard deviation =", math.sqrt(Weighted_Covariance))


# - d
# 
# The gambler investor would choose the portfolio b since it yeilds the highest expected return.
# 
# - e
# 
# The risk-averse investor would choose the portfolio a since it yeilds the lowest standard deviation.

# ### 7.109
# - a

# In[2]:


p = 0.3
n = 25
def Bernoulli(n, p, x):
    return math.comb(n, x)*pow(p, x)*pow((1 - p), n - x)

sum = 0
for i in range(0,11):
    sum += Bernoulli(n, p, i)

print("P(10 or fewer customers chose the leading brand) = ", sum)


# - b

# In[3]:


sum = 0
for i in range(11,26):
    sum += Bernoulli(n, p, i)

print("P(11 or more customers chose the leading brand) = ", sum)


# - c

# In[5]:


print("P(10 customers chose the leading brand) = ", Bernoulli(n, p, 10))


# ### 7.127
# - a

# In[6]:


n = 100
p = 0.53
sum = 0
for i in range(1, 51):
    sum += Bernoulli(n, p, i)
    
print("P(more than half say that Congress is doing a poor or bad job) = ", 1 - sum)


# - b

# In[7]:


sum = 0
for i in range(1, 61):
    sum += Bernoulli(n, p, i)
    
print("P(more than 60% say that Congress is doing a poor or bad job) = ", 1 - sum)


# - c
# 
# $E(X) = np = 53$(people)

# ### 7.133
# - a
# 

# In[16]:


def Poison(mu, x):
    factorial = 1
    for i in range(1, x+1):
        factorial *= i;
    return math.exp(-mu) * pow(mu, x) / factorial

sum = 0
for i in range(0, 10):
    sum += Poison(5, i)
print("P(the site gets 10 or more hits in a week) = ", 1 - sum)


# - b

# In[17]:


sum = 0
for i in range(0, 20):
    sum += Poison(10, i)
    
print("P(the site gets 20 or more hits in 2 weeks) = ", 1 - sum)


# ### 7.141
# - a

# In[18]:


print("P(A golfer loses no golf balls) = ", Poison(2, 0))


# - b

# In[19]:


sum = 0
for i in range(0, 4):
    sum += Poison(2, i)
    
print("P(A golfer loses 4 or more golf balls) = ", 1 - sum)


# - c

# In[20]:


sum = 0
for i in range(0, 3):
    sum += Poison(2, i)
    
print("P(A golfer loses 2 or fewer golf balls) = ", sum)


# ## All problems in the hw 6 is solved, and my answers are shown as above. Thank TAs for reading and checking my homework!
# ps. If my homework page is still too dark to read, please inform me or check from my github repository: https://github.com/ujkuo/NTU-IM-Stat
