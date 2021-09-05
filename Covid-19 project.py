#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df= pd.read_csv('C:/Users/UT/Desktop/Covid-19 Project/country_vaccinations.csv')


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


col=df.shape[1]
rows=df.shape[0]
datasize= df.shape
print("Total number of rows= ", rows)
print("Total number of columns= ", col)
print("Size", datasize)


# In[6]:


null= df.isnull().values.any()
nullval= df.isnull().sum()
nullval


# In[20]:


dataframe=df.fillna(0)
dataframe
dataframe.to_excel("output.xlsx") 


# In[8]:


dataframe.describe().transpose()


# In[19]:


vaccine= dataframe.groupby(['country'])['total_vaccinations'].sum().reset_index()
vaccine = vaccine.nlargest(20, ['total_vaccinations']).reset_index()
del vaccine['index']
vaccine


# In[ ]:





# In[31]:


plt.figure(figsize=(15,10))
sns.barplot(y=vaccine['country'],x=vaccine['total_vaccinations'])


# In[36]:


vaccince_types = dataframe.groupby(['vaccines'])['country'].unique()
vaccince_types = vaccince_types.reset_index()
vaccince_types


# In[52]:


pd = dataframe.groupby(["vaccines"]).sum()
pd = pd.sort_values(by=['total_vaccinations'], ascending=False)
pd


# In[53]:


fig ,ax = plt.subplots(figsize=(15,7))

#2 Plotting data
p1 = ax.bar(pd.head(15).index, pd.head(15)['total_vaccinations'], color='teal', label='Vaccination', width=0.4)

#3 Customize the plot
plt.ylim(0 ,1300000000)
plt.xticks(rotation = 90);
ax.set(xlabel='Name of vaccine', ylabel='Total vaccine', title='Usage of diffrent vaccine');
ax.xaxis.label.set_color('black')


#4 Add legend
plt.legend()

#4 Use plot style
plt.style.use('seaborn-whitegrid')


# In[56]:


top_country= dataframe.groupby(['country'])['total_vaccinations_per_hundred'].sum().reset_index()
top_country = top_country.nlargest(20, ['total_vaccinations_per_hundred']).reset_index()
del top_country['index']
top_country


# In[61]:


plt.figure(figsize=(15,10))
sns.barplot(y=top_country['country'],x=top_country['total_vaccinations_per_hundred'])

