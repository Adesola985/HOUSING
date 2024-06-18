#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd


# In[2]:


pwd


# In[3]:


crude = pd.read_csv('crude.csv')


# In[4]:


crude


# In[5]:


crude.head()


# In[6]:


crude.info()


# In[7]:


crude ['ocean_proximity'].value_counts()


# In[8]:


crude.describe()


# In[9]:


import matplotlib.pyplot as plt


# In[10]:


crude.hist(bins=50, figsize=(22,17))
plt.show()


# In[12]:


from sklearn.model_selection import train_test_split
train_set, test_set = train_test_split(crude, test_size= 0.2)


# In[13]:


train_set.info()


# In[14]:


test_set.info()


# In[15]:


test_set.head()


# In[16]:


crude= train_set.copy()


# In[17]:


crude.plot (kind= 'scatter', x= 'longitude', y= 'latitude')


# In[18]:


crude.plot (kind= 'scatter', x= 'longitude', y= 'latitude', alpha = 0.1)


# In[19]:


crude.plot (kind= 'scatter', x= 'longitude', y= 'latitude', alpha = 0.4, s=crude ['population']/100, label ='population',
            figsize = (10,7), c='median_house_value', cmap=plt.get_cmap('jet'), colorbar=True, 
            sharex = False)
plt.legend()


# In[20]:


crude


# In[22]:


crude['rooms_per_household'] = crude['total_rooms']/crude['households']
crude['population_per_house'] = crude['population']/crude['households'] 


# In[29]:


crude.plot(kind='scatter', x= 'rooms_per_household', y = 'median_house_value', alpha
plt.axis([0,5, 0, 520000])
           plt.show()


# In[28]:


plt.show()


# In[25]:


crude


# In[21]:


crude.describe().T


# In[ ]:




