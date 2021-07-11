#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[12]:


xls = pd.ExcelFile('C:/Users/Vinayak BB/Desktop/Datasets/Virtual_Gaming.xlsx')
df1 = pd.read_excel(xls, 'User Demographics')
df2 = pd.read_excel(xls, 'Daily User-wise Revenue data')


# In[13]:


df1,df2


# In[17]:


df2.rename(columns={"User id":"User Id"},inplace=True)
df1.rename(columns={"State (entered by user)":"State"},inplace=True)


# In[18]:


df1,df2


# In[33]:


df3 =pd.merge(df1,df2,on="User Id")
df4=df3.groupby(["User Id"]).first()


# In[51]:


df5=df3.groupby(["State"]).sum()
df5


# In[54]:


Q1=df5.sort_values(["Revenue collected"],ascending=False)[0:5]
Q1#question1-Top5 states in terms of revenue


# In[71]:


display(Q1)


# In[119]:


df5=df3.groupby(["Date"]).sum()[0:5]
df5.sort_values("Revenue collected",ascending=False)#revenue collected by date top first five


# In[120]:


df3["Date"].value_counts().mean()#Q2 Answer Avg number of User Active Per Day


# In[189]:


A=df1['User Id'].value_counts().sum()
A#number of user


# In[199]:


df3.groupby(['Date']).mean()#Revenue Collected Per Day


# In[204]:


df3.groupby(['User Id','Date']).mean()
#Q3-Avg Revenue Collected Per User Per Day


# In[205]:


df3.groupby(['Date','User Id']).mean()
#Avg Revenue Collected Per Day Per User


# In[ ]:




