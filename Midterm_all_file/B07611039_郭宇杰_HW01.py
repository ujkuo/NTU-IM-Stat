#!/usr/bin/env python
# coding: utf-8

# # Stat HW01 by 郭宇杰, B07611039
# 

# ### 1.3
# - (a) 25,000 registered voters
# - (b) 200 registered voters interviewed
# - (c) The value 48% is a statistic, since the 200 registered interviewed voters are sample instead of population. As a result, it is not a parameter but a statistic.

# ### 1.6
# ...OK I understand its words.

# ### 1.7
# - (a) If the probability of success on head or tail is not 0.5 or near 0.5, we could conclude that this coin is a biased coin since the number of heads 95 is a lot of greater than 50.
# - (b) If the probability of success on head or tail is 0.5 or near 0.5, we could conclude that this coin is an unbiased coin.
# - (c) My answer is "NO" since the statement says I will "always" observe "exactly" 50 heads. The use of these two words are so arrogant. I think the number from 40 to 60 is a reasonable range, but it is just a rough estimate.

# ### 2.5
# - (a) The age is belongs to interval data.
# - (b) The floor of residents' condominium is belongs to ordinal data.
# - (c) This is belongs to nominal data.
# - (d) This is belongs to ordinal data.
# - (e) This is belongs to nominal data.

# ### 2.11
# - (a) This is belongs to nominal data.
# - (b) This is belongs to interval data.
# - (c) This is belongs to ordinal data.

# ### 2.13

# In[1]:


# import necessary libraries
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm
from matplotlib.ticker import FuncFormatter
from matplotlib.pyplot import figure
import pandas as pd
import numpy as np


# In[2]:


df_c2_3 = pd.read_excel('Xr02-13.xlsx') #read file


# In[3]:


country = df_c2_3["Country"]
reserves = df_c2_3["Oil Reserves (Barrels)"] # read column value


# In[4]:


def billions(x,pos):
    return '%1.1fM' % (x * 1e-9)


# In[7]:


x = np.arange(15)
formatter = FuncFormatter(billions)
fig, ax = plt.subplots(figsize=(12,8))
rectsb = ax.bar(country, reserves, width=0.5, bottom=None, align='center')
ax.yaxis.set_major_formatter(formatter)

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        plt.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


for index,data in enumerate(reserves):
    plt.text(x=index , y =data+1 , s=f"{data}" , fontdict=dict(fontsize=10), rotation = 60)
        
plt.bar(x, reserves)
plt.xticks(x,(country))
plt.xticks(rotation = 60)
plt.title('Bar Chart for oil reserves')        
#autolabel(rectsb)
plt.show()


# The bar chart is shown as above.

# ### 2.29
# - (a)

# In[8]:


data2_29 = pd.read_excel('Xr02-29.xlsx')
newspaper = data2_29["Newspaper"]
from texttable import Texttable


# In[9]:


# count frequency
frequency = {}
total = 0
for item in newspaper:
    total += 1
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print(frequency)
print(frequency.values())
print(total)
id = ["1","2","3","4"]
frequency = [128,141,32,49]
relative = []
for i in range(4):
    relative.append(frequency[i] / total)
    print('{:.2f}'.format(relative[i]))
#df = pd.DataFrame(frequency, index = id)
#print(df)


# In[10]:


t = Texttable()
t.add_rows([['Newspaper','Code','Frequency','relative frequency distribution'],['NewYorkDailyNews',1,128,relative[0]],['NewYorkPost',2,141,relative[1]],['NewYorkTimes',3,32,relative[2]],['WallStreetJournal',4,59,relative[3]]])
print(t.draw())


# The result is shown as below with a table form.

# - (b)

# In[11]:


labels = 'NewYorkDailyNews', 'NewYorkPost', 'NewYorkTimes', 'WallStreetJournal'
sizes = [128, 141, 32, 59]
explode = (0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.2f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


# I choose the pie chart as an appropriate to summarize the data. As the pie chart shown above, we can find that the New York Post and New York Daily News are the most popular news in the markets.

# ### 2.41

# In[12]:


data2_41 = pd.read_excel('Xr02-41.xlsx')
data_less = list(data2_41.iloc[0])
data_high = list(data2_41.iloc[1])
data_some = list(data2_41.iloc[2])
data_college = list(data2_41.iloc[3])

# use a dumb method to filter data = =
num_less = []
num_high = []
num_some = []
num_college = []
for i in range(len(data_less)): # eliminate the first element in the list
    if i == 0:
        continue
    num_less.append(data_less[i])
    num_high.append(data_high[i])
    num_some.append(data_some[i])
    num_college.append(data_college[i])


# In[13]:


# use a dumb method to filter data = =
data_2000 = [num_less[0], num_high[0], num_some[0], num_college[0]]
data_2005 = [num_less[1], num_high[1], num_some[1], num_college[1]]
data_2010 = [num_less[2], num_high[2], num_some[2], num_college[2]]
data_2015 = [num_less[3], num_high[3], num_some[3], num_college[3]]


# In[14]:


labels = ['2000', '2005', '2010', '2015']

x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots(figsize=(12,8)) # set size
rects1 = ax.bar(x - 3*width/2, num_less, width, label='Less than high school')
rects2 = ax.bar(x - width/2, num_high, width, label='High school')
rects3 = ax.bar(x + width/2, num_some, width, label='Some college')
rects4 = ax.bar(x + 3*width/2, num_college, width, label='College graduate')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('People')
ax.set_title('Years')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


# deal with the corresponding bar
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)

fig.tight_layout()

plt.show()


# In[15]:


labels = ['Less than high school', 'High school', 'Some college', 'College graduate']

x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots(figsize=(12,8)) # set size
rects1 = ax.bar(x - 3*width/2, data_2000, width, label='2000')
rects2 = ax.bar(x - width/2, data_2005, width, label='2005')
rects3 = ax.bar(x + width/2, data_2010, width, label='2010')
rects4 = ax.bar(x + 3*width/2, data_2015, width, label='2015')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('People')
ax.set_title('Years')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)

fig.tight_layout()

plt.show()


# I'm not sure which bar charts above is better to demonstrate the educational level of adults change over the past 15 years, but both two bar charts show that as time passing, adults who have taken the education become higher. Also, I think that we can conclude by charts that there is large number of Americans go to college.

# ### 2.51

# In[16]:


data2_51 = pd.read_excel('Xr02-35.xlsx')
share = data2_51["Share"]
political_view = data2_51["Political View"] # read date

num_share, num_pv = (4,3) # create a 2-d list
frequency = []
for i in range(num_pv):
    col = []
    for j in range(num_share):
        col.append(0)
    frequency.append(col)

# count total times and frequency
total = 0
for item in share:
    total += 1

for i in range(total):
    value1 = share[i]
    value2 = political_view[i]
    frequency[value2-1][value1-1] += 1

# print(frequency)

share1 = []
share2 = []
share3 = []
share4 = []

# use a dumb way to filter data = =
for i in range(num_share):
    if i == num_share:
        break
    share1.append(frequency[i-1][0])
    share2.append(frequency[i-1][1])
    share3.append(frequency[i-1][2])
    share4.append(frequency[i-1][3])
    
share1.pop(0)
share2.pop(0)
share3.pop(0)
share4.pop(0)


# In[17]:


labels = ['Political View 1', 'Political View 2', 'Political View 3']

x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots(figsize=(12,8)) # set size
rects1 = ax.bar(x - 3*width/2, share1, width, label='Share = 1')
rects2 = ax.bar(x - width/2, share2, width, label='Share = 2')
rects3 = ax.bar(x + width/2, share3, width, label='Share = 3')
rects4 = ax.bar(x + 3*width/2, share4, width, label='Share = 4')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Political View')
ax.set_title('Share')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)

fig.tight_layout()

plt.show()


# The row labels show the political views, which are:
# - 1. Conservative
# - 2. Moderate
# - 3. Liberal
# And the column labels show the shares, which are:
# - 1. Fair share
# - 2. Too much
# - 3. Too little
# - 4. No opinion
# 
# From the above chart, we can conclude that among these three groups, they all think upper-income people are paying too little taxes. But in the conservative group, people have more likely to say it's a fair share than moderate and liberal.

# ## All problems in the hw 1 is solved, and my answers are shown as above. Thank TAs for reading and checking my homework!

# In[ ]:




