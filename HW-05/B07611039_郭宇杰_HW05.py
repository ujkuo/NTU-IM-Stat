#!/usr/bin/env python
# coding: utf-8

# # Stat HW05 by 郭宇杰, B07611039

# In[1]:


import ete3
import numpy as np


# In[2]:


from ete3 import Tree


# In[1]:


get_ipython().system('pip install ete3')


# In[3]:


from ete3 import Tree, faces, TreeStyle, TextFace


# ### 6.3
# 
# - a
# 
# The sample space is $S = \{ a,b,c,d,e \}$ where denote $a, b, c, d, e$ as five possible answers for a multiple-choice-question.
# 
# - b 
# 
# $P(a) = P(b) = P(c) = P(d) = P(e) = \frac{1}{5}$
# 
# - c
# 
# classical approach
# 
# - d 
# 
# Since we have 5 options and the probability of each option is equal.

# ### 6.17
# - a

# In[3]:


sum = 38.4 + 3.0 + 1.6 + 1.4 + 1.3 + 1.1 + 15.2
print("P(Individual speaks Spanish) = ", 38.4 / sum)


# - b

# In[4]:


print("P(Individual speaks a language other than Spanish) = ", 1 - (38.4 / sum))


# - c

# In[5]:


print("P(Individual speaks Vietnamese or French) = ", (1.4 + 1.3) / sum)


# - d

# In[6]:


print("P(Individual speaks one of the other languages) = ", 15.2 / sum)


# ### 6.31
# - a

# In[7]:


print("The rate of promotion among female assistant professors is ", 0.03 / (0.03 + 0.12) )


# - b

# In[8]:


print("The rate of promotion among male assistant professors is ", 0.17 / (0.17 + 0.68) )


# - c
# By observing the rate of promotions among female and male assistant professors, it can be concluded taht no gender biasedness in the university.

# ### 6.39
# - a
# 
# P(25- to 54-year-old employee was laid off or fired because of insufficient work) = 0.18
# 
# - b

# In[10]:


print("The proportion of laid-off or fired workers is age 65 and older is", 0.029 + 0.011 + 0.016)


# - c

# P(a laid-off or fired worker because the plant or company closed is 65 or older) = 0.029

# ### 6.55
# 
# - a

# In[11]:


print("P(one respondent selected at random would trust NBC News) is ", 0.0896 + 0.1386 + 0.1944 + 0.0629 + 0.0144)


# - b
# 
# P(a consistent Conservative would distrust NBC News) = 0.0558
# 
# - c
# 
# P(a consistent Liberal neither trusts nor distrusts NBC News) = 0.0576
# 
# - d

# ### 6.69
# Let $B$ = line is bust, $B^C$ = line is not busy, $S$ = sale, $S^C$ = does not sale.
# $P(S) = P(S | B^C) * P(B^C) = 0.05 * (1 - 0.2) = 0.04$

# ### 6.75
# 

# In[12]:


print("P(a person is a consistent Liberal) = ", 0.0896 + 0.0096 + 0.0576 + 0.0032)


# ### 6.83

# In[13]:


print("Probability is ", (630 / 1700) * 0.62 + (590 / 1700) * 0.74 + (480 / 1700) * 0.57)


# ### 6.91
# From the statement, we have
# P(BAC = 0 | Crash with fatality) = 0.616
# P(BAC is between 0.01 and 0.09 | Crash with fatality) = 0.300
# P(BAC is greater than 0.09 | Crash with fatality) = 0.084
# P(Crash with fatality) = 0.01
# P(BAC is greater than 0.09) = 0.12
# 
# P(crash with fatality | BAC is greather than 0.09) = P(crash with fatality and BAC is greather than 0.09) / P(BAC is greather than 0.09) = 0.084 * 0.01 / 0.12 = 0.007
# 
# So the answer is 0.007.
