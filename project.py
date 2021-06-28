#!/usr/bin/env python
# coding: utf-8

# In[54]:


#TO ACCESS THE DATAFRAME USING PANDAS FUNCTION
import pandas as pd
import numpy as np
import seaborn as sb
titanic=pd.DataFrame(pd.read_csv(r"C:\Users\user\Desktop\Titanic_ship.csv"))
print("Titanic_Ship is  type of:",type(titanic))#it gives the type of data frame
print("Titanic_Ship have a shape of:",titanic.shape)#it represents a how many rows and colomns present in data frame


# In[55]:


titanic.head()#TO ACCESS THE first five  ROWS  of LARGE DATA FRAMES


# In[48]:


a=titanic.head(10)#TO ACCESS THE SPECIFIC SET OF ROWS IN LARGE DATA FRAMES


# In[ ]:





# In[56]:


titanic['Survived']#To get entire data of specific COLOUMN


# In[29]:


titanic.count()#to count the number of non NAN values in every coloumn


# In[31]:


titanic.count(axis=1)#To count the number of non NAN values in every ROW


# In[32]:


titanic.tail()##TO ACCESS THE last SET OF ROWS IN LARGE DATA FRAMES


# In[35]:


titanic.isnull().sum()#to count the number of nan values in every column


# In[8]:


titanic['Pclass'].describe()#IT GIVES THE HOW MANY PASSENGERS ARE PRESENT IN THAT SHIP ACCORDING TO CLASSES


# In[66]:


sb.countplot(data=a,x='PassengerId')


# In[21]:


a['Age'].fillna('0')


# In[58]:


titanic.fillna('0')
titanic.isnull().sum()


# In[61]:


base.color=sb.color_palette([3])
sb.counterplot(data=titanic,x='age>14',color=base_color)


# In[ ]:




