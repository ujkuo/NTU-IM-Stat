#!/usr/bin/env python
# coding: utf-8

# # Stat HW02 by 郭宇杰, B07611039

# ### 3.5 Draw a histogram with the given data.

# In[6]:


import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm
from texttable import Texttable as tt
from matplotlib.ticker import FuncFormatter
from matplotlib.pyplot import figure
import pandas as pd
import numpy as np
import seaborn as sns ### packages below should be installed into the class_usb
import scipy.stats as stats
import statsmodels.api as sm
import statsmodels.stats.api as sms
import statsmodels.formula.api as smf


# In[7]:


data_3_5 = pd.read_excel('Xr03-05.xlsx')


# In[8]:


### codes below are copied from prof's slide
plt.rcParams["figure.dpi"] = 80
bins_list = []
for i in range(21):
    if i%4 == 0 or i == 20:
        bins_list.append(i)
# bins_list = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
fig, ax = plt.subplots()
counts, bins, patches = plt.hist(data_3_5["Calls"], bins=bins_list, density=False, facecolor='g', alpha=0.75)
mu = np.mean(data_3_5["Calls"])
sigma = np.std(data_3_5["Calls"])
plt.xlabel('Amount of Calls')
plt.ylabel('Frequency')
plt.title('Histogram of Calls')
# plt.text(60, .025, r'$\mu = $', mu,'$\sigma = $', sigma)
plt.grid(True) # 格線顯示
plt.xticks(bins_list)
bin_centers = [np.mean(k) for k in zip(bins[:-1], bins[1:])]
#ax.plot(bin_centers, counts.cumsum(), 'ro-') # show 折線
plt.show()


# The histogram for 3.5 is shown above.

# ### 3.11 Draw a histogram and describe its shape.

# In[41]:


data_3_11 = pd.read_excel('Xr03-11.xlsx')


# In[128]:


num_of_attended_games = data_3_11["Games"]
### codes below are copied from prof's slide
plt.rcParams["figure.dpi"] = 80
bins_list = []
for i in range(33):
    if i==0:
        continue
    if i%4 == 0:
        bins_list.append(i)
# bins_list = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
fig, ax = plt.subplots()
counts, bins, patches = plt.hist(data_3_11["Games"], bins=bins_list, density=False, facecolor='g', alpha=0.75)
mu = np.mean(data_3_11["Games"])
sigma = np.std(data_3_11["Games"])

plt.xlabel('The Amount of Games')
plt.ylabel('Frequency')
plt.title('A survey of 50 baseball fans to report the number of games they attended last year')


# plt.text(60, .025, r'$\mu = $', mu,'$\sigma = $', sigma)
plt.grid(True) # 格線顯示
plt.xticks(bins_list)
bin_centers = [np.mean(k) for k in zip(bins[:-1], bins[1:])]
# ax.plot(bin_centers, counts.cumsum(), 'ro-') # show 折線
plt.show()


# The result shows that most surveyed fans attend games with the frequency from 4 to 16, and the hisgram is positively skrewed.

# ### 3.17

# In[43]:


data_3_17 = pd.read_excel('Xr03-17.xlsx')

### codes below are copied from prof's slide
plt.rcParams["figure.dpi"] = 80
bins_list = []
for i in range(30,101):
    if i%8 == 2:
        bins_list.append(i)

fig, ax = plt.subplots()

counts, bins, patches = plt.hist(data_3_17["Marks"], bins=bins_list, density=False, facecolor='g', alpha=0.75)
mu = np.mean(data_3_11["Games"])
sigma = np.std(data_3_11["Games"])

plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.title('The marks of 320 students on an economics midterm test')


plt.grid(True) # 格線顯示
plt.xticks(bins_list)
bin_centers = [np.mean(k) for k in zip(bins[:-1], bins[1:])]
# ax.plot(bin_centers, counts.cumsum(), 'ro-') # show 折線
plt.show()


# The graph is multi-modal, and it tells us that the most students get the makr between 74 to 90, and another majority of students get between 34 to 58.

# ### 3.39
# - (a)

# In[44]:


data_3_39a = pd.read_excel('Xr03-39.xlsx')

year = data_3_39a['Year']
DI = data_3_39a['Disability Ins (DI) -fed']

plt.title('SSDI(Social Security Disability Insurance) costs recorded for the years 1958 to 2015')
plt.xlabel('Year')
plt.ylabel('Disability Ins (DI) -fed')

plt.plot(year,DI)

plt.show()


# It can be seen that the SSDI costs has increased from 1958 to 2015.

# - b

# In[129]:


data_3_39b = pd.read_excel('Xr03-39.xlsx')
people = pd.read_excel('U.S. Population 1935-2015.xlsx')
# fig = plt.subplots(figsize=(10, 2))
# plt.ylim(0, 1)

year = data_3_39b['Year']

DI_per_capita = np.zeros(shape=(58))
# print(value)
for i in range(0, 58):
    DI_per_capita[i] = data_3_39b.iloc[i, 1] * 1000 / people.iloc[i+23, 1] 

# plt.grid(True)
plt.plot(year, DI_per_capita)
plt.title('SSDI(Social Security Disability Insurance) costs per capita recorded for the years 1958 to 2015')
plt.xlabel('Year')
plt.ylabel('DI Cost per capita')
plt.show()


# The shart shows that the SSDI costs per captia has also increased from 1958 to 2015.

# - c

# In[49]:


data = pd.read_excel('Xr03-39.xlsx')
people = pd.read_excel('U.S. Population 1935-2015.xlsx')
cpi = pd.read_excel('U.S. CPI Annual.xlsx')

year = data['Year']

DI_new = np.zeros(shape=(58))

for i in range(0, 58):
    DI_new[i] = (data.iloc[i, 1] * 100 * 1000 / people.iloc[i+23, 1]) / cpi.iloc[i + 45, 1]

plt.plot(year, DI_new)
plt.title('SSDI(Social Security Disability Insurance) costs per capita in\n constant 1982–1984 dollars recorded for the years 1958 to 2015')
plt.xlabel('Year')
plt.ylabel('DI Costs per capita in constant 1982–1984 dollars')
plt.show()


# The pattern of the chart is same as the chart in 3-a, 3-b, which is also increasing as time gone by. (I'm not sure how to describe the minor decrease from 1975 to 1980, I have checked the origin data but nothing weird in the trend of data, so I decide to give no explaination for that. Hope it's not very important for the chart description QQ.)

# ### 3.47

# In[130]:


data_3_47 = pd.read_excel('Xr03-47.xlsx')

year = data_3_47['Year']
consumption = data_3_47['Consumption']
production = data_3_47['Production']

plt.plot(year, consumption, label = "Consumption")
plt.plot(year, production, label = "Production")

plt.title('The average daily U.S. oil consumption and production')
plt.xlabel('Year')
plt.ylabel('Oil Consumption & Production (thousands of barrels)')
plt.legend()

plt.show()


# It can easily be seen that the orange line is always below the blue time, that means consumption of oil is very high in comparison with the production of oil in US. But the trend of the orange line increased after 2010.

# ### 3.53

# In[62]:


data_3_53 = pd.read_excel('Xr03-53.xlsx')

year = data_3_53["Year"]
month = data_3_53["Month"]

plt.plot(data["Japanese Yen to one U.S. Dollar"])
plt.title('The exchange rate of Japanese Yen to one U.S. Dollar from 1971 to 2016')
plt.xlabel('Month')
plt.ylabel('The exchange rate of Japanese Yen \n to one U.S. Dollar')

plt.show()


# The chart shows that the exchange rate of Japanese Ten to one U.S. Dolar is decreasing as time gone by. There are some increasing pattern in the chart but it doesn't influence the trend of decreasing pattern.

# ### 3.63

# In[83]:


data_3_63 = pd.read_excel('Xr03-63.xlsx')

plt.scatter(data_3_63['Temperature'], data_3_63['Tickets'], color = 'r')

plt.xlabel('Temperature')
plt.ylabel('Tickets')
plt.title('Scatter diagram with a linear line of the relationship \n between number of tickets sold and temperature.')

linear_line = sns.regplot(x='Temperature', y= 'Tickets', data = data_3_63, color = 'r', ci = None)
plt.show()


# With only scatter plots, it's hard to give a precise observation. However, if we add a linear regression line to help us describe the scatter diagram, we can find that the tickets sold more with the increasing of temperature. It's reasonable since all of us don't want go skiing in a very low temperature (at least I do).

# ### 3. 67
# - a

# In[131]:


data_3_67 = pd.read_excel('Xr03-67.xlsx')

plt.title('Scatter diagram of the relationship \n between sales and time between movie showing.')
plt.xlabel('Time length')
plt.ylabel('Sales')

plt.scatter(data_3_67['Time'], data_3_67['Sales'], color = 'r')
# linear_line = sns.regplot(x='Time', y= 'Sales', data = data_3_67, color = 'r', ci = None)
plt.xlim(5, 35)
plt.show()


# - b

# In[140]:


data_3_67 = pd.read_excel('Xr03-67.xlsx')

plt.title('Scatter diagram of the relationship \n between sales and time between movie showing.')
plt.scatter(data_3_67['Time'], data_3_67['Sales'], color = 'r')
linear_line = sns.regplot(x='Time', y= 'Sales', data = data_3_67, color = 'r', ci = None)
plt.xlabel('Time length') # The position will change the result, if we add this line before reg, it will not show the lable.
plt.ylabel('Sales')
plt.xlim(5, 35)
plt.show()


# With the origin scatter plots and an extra linear regression line for helping easier observation, we can say that there is no positive relationship between two variables.

# ### 3.83
# - a

# In[139]:


data_3_83 = pd.read_excel('Xr03-83.xlsx')

print("The injury rate (per 100 accidents) for each age group: \n" )
injure_rate = []
#t = Texttable()
for i in range(9):
    table = []
    injure_rate.append(data_3_83.iloc[i, 2] / (data_3_83.iloc[i, 1] / 100))
    table.append(data_3_83.iloc[i, 0])
    table.append(injure_rate[i])
    #t.add_rows(table)
    print(data_3_83.iloc[i, 0], ":", injure_rate[i], "\n")
    
#print(t.draw())
print("\nThe death rate (per accident) for each age group: \n" )
death_rate = []
for i in range(9):
    death_rate.append(data_3_83.iloc[i, 3] / data_3_83.iloc[i, 1])
    print(data_3_83.iloc[i, 0], ":", death_rate[i], "\n")


# (I originally decided to use the package to draw a pretty table for the data description, but something is broken and I have no time to fix and check for it so that I have no choice but to present the data in an easy way.)

# - b

# In[5]:


data_3_83 = pd.read_excel('Xr03-83.xlsx')

injure_rate = []
death_rate = []
for i in range(9):
    injure_rate.append(data_3_83.iloc[i,2] / data_3_83.iloc[i,1])
    death_rate.append(data_3_83.iloc[i,3] / data_3_83.iloc[i,1])
    
age = data_3_83['Age group']

plt.title('the injury rate and the death rate for each age group')
plt.xlabel('Age Group')
plt.ylabel('injury rate (per 100 accidents) \n and the death rate (per 100 accidents)')

plt.plot(age, injure_rate, label = "Injury Rate")
plt.plot(age, death_rate, label = "Death Rate")

x = []
for i in range(9):
    x.append(data_3_83.iloc[i, 0])
    
plt.xticks(rotation = 60)
plt.legend() # show the block
plt.show()


# From the chart, we can see that the elder group has the higher injury and death rate, and the younger has the lower.

# ## All problems in the hw 1 is solved, and my answers are shown as above. Thank TAs for reading and checking my homework!
