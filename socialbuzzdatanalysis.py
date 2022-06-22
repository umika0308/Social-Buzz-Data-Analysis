#!/usr/bin/env python
# coding: utf-8

# In[72]:


import numpy as np
import pandas as pd
import datetime
import calendar
import matplotlib.pyplot as plt


# In[2]:


d1=pd.read_csv('Content.csv')
d2=pd.read_csv('Reactions.csv')
d3=pd.read_csv('ReactionTypes.csv')
d4=pd.read_csv('User.csv')
d5=pd.read_csv('Session.csv')
d6=pd.read_csv('Profile.csv')
d7=pd.read_csv('Location.csv')


# In[3]:


d1.head(1)


# In[4]:


d2.head(5)


# In[5]:


d3.head(1)


# In[6]:


d1.drop('Unnamed: 0',axis=1,inplace=True)
d2.drop('Unnamed: 0',axis=1,inplace=True)
d3.drop('Unnamed: 0',axis=1,inplace=True)


# In[7]:


d1.drop('URL',axis=1,inplace=True)


# In[8]:


df1=pd.merge(d1,d2,on=('Content ID'),how='left')


# In[9]:


df1


# In[10]:


df1.rename(columns={'Type_x': 'Content Type', 'Reaction Type':'Type','User ID_x':'User ID','User ID_y':'Reactor User ID'},inplace=True)


# In[11]:


df1


# In[12]:


df=pd.merge(df1,d3,on=('Type'),how='left')


# In[ ]:


df


# In[ ]:


d3.head(1)


# In[ ]:


df.isnull().sum()


# In[ ]:


df1.drop('Reactor User ID',axis=1,inplace=True)


# In[13]:


df.rename(columns={'Type':'Reaction Type'},inplace=True)


# In[14]:


df


# In[15]:


df.isnull()


# In[16]:


df = df.dropna(subset=['Reaction Type', 'Sentiment','Score'],how='all')


# In[17]:


df


# In[87]:


df.to_csv('file1.csv')


# In[18]:


df.rename(columns={'Type':'Reaction Type'},inplace=True)


# In[19]:


cat=df.groupby('Category')['Category'].count()


# In[20]:


print(cat)


# In[21]:


dm=pd.read_csv('dm.csv')


# In[22]:


dm


# In[23]:


dm.drop('Unnamed: 0',axis=1,inplace=True)


# In[24]:


dm


# In[25]:


cat=dm.groupby('Category')['Category'].count()


# In[110]:


print(cat)


# In[111]:


cat.sort_values(ascending=False)


# In[28]:


a1=dm.groupby(['Category']).sum()


# In[33]:


a1.sort_values(by=['Score'],ascending=False)


# In[ ]:





# In[57]:


dm.drop('Month',axis=1,inplace=True)


# In[ ]:





# In[58]:


dm


# In[60]:


dm.drop('month',axis=1,inplace=True)


# In[62]:


dm.rename(columns={'Datetime':'Month'},inplace=True)


# In[63]:


dm


# In[66]:


dm['Month'] = dm['Month'].apply(lambda x: calendar.month_abbr[x])


# In[67]:


dm


# In[69]:


dm['Month'].value_counts(ascending=False)


# In[70]:


p=pd.DataFrame({'Category':['Animals','Science','Healthy Eating','Technology','Food'],'Scores':[74965,71168,69339,68738,66676]})


# In[75]:


p.groupby(['Category']).sum().plot(
    kind='pie', y='Scores', autopct='%1.1f%%')


# In[81]:


labels='Animals','Science','Healthy Eating','Technology','Food'
sizes=[74965,71168,69339,68738,66676]


# In[83]:


fig1,ax1=plt.subplots()
ax1.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
ax1.axis('equal')
plt.title('Top 5 categories based on popularity')
plt.show()


# In[ ]:




