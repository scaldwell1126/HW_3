#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import datetime as dt
file = "Resources/budget_data.csv"

df = pd.read_csv(file)
df.head()


# In[4]:


unique_date = df["Date"].unique()


# In[5]:


df.count()


# In[6]:


df.dtypes


# In[7]:


df['Date'].unique()


# In[8]:


df['Date'] = pd.to_datetime(df['Date'])   


# In[9]:


total_months = df['Date'].nunique()
total_months


# In[19]:


total = df['Profit/Losses'].sum()
total


# In[47]:





# In[11]:


df['Change'] = df['Profit/Losses'].diff()#.fillna(df['Profit/Losses'])


# In[12]:


df['Change']


# In[13]:


greatest_increase = df['Change'].max()
greatest_increase


# In[45]:




        


# In[15]:


greatest_decrease = df['Change'].min()
greatest_decrease


# In[17]:


average_change = df['Change'].mean()
average_change


# In[20]:


#Financial_Analysis_Output 
print('Financial Analysis')
print("--------------------------------")
print(f"Total Months: " + str(total_months))
print(f"Total: " + str(total))
print(f"Average Change: " + str(average_change))
print(f"Greatest Increase in Profits: " + str(greatest_increase))
print(f"Greatest Decrease in Profits: " + str(greatest_decrease))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




