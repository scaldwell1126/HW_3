#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
import numpy as np
file = "Resources/election_data.csv"
df = pd.read_csv(file)
df.head()
df.info()


# In[21]:


total_votes = df['Voter ID'].nunique()
total_votes


# In[22]:


candidate = df['Candidate'].value_counts()
candidate 


# In[23]:


candidate_list = candidate.tolist()
candidate_list


# In[24]:


Khan_average = 2218231/3521001
Khan_avg = "{0:.0%}".format(2218231/3521001)
print (Khan_avg)


# In[25]:


Correy_avg = "{0:.0%}".format(704200/3521001)
print (Correy_avg)


# In[26]:


Li_avg = "{0:.0%}".format(492940/3521001)
print (Li_avg)


# In[27]:


OTooley_avg = "{0:.0%}".format(105630/3521001)
print(OTooley_avg)


# In[17]:


election_results = {
                    "Candidates ": ["Khan", "Correy", "Li","O'Tooley"],
                    "% of Vote ": ["63.00%", "20.00%", "14.00%", "3.00%" ],
                    "# of Votes ": [2218231, 704200, 492940, 105630]
}
info_pd = pd.DataFrame(election_results)#, columns=["candidates", "percentage", "votes"])
info_pd    


# In[19]:


print("Election Results")
print("------------------------------------------")
print(info_pd)
print("-------------------------------------------")
print("Winner: Khan")
print("--------------------------------------------")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[39]:


cand_group = df.groupby(['Candidate'])
cand_group.mean()


# In[28]:





# In[42]:


def square(number):
    return number * number
    squared = square(2)
    print(squared)


# In[46]:


df['count'] = df['Candidate'].count()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




