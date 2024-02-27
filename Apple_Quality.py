#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Following Libraries are being used
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# In[2]:


# Load training data
data = pd.read_csv('apple_quality.csv')
data.head()


# In[3]:


# Check dimensions of the data
data.shape


# In[5]:


df = pd.read_csv('apple_quality.csv')


# In[6]:


# Description
data.describe()


# In[7]:


# Check Datatypes
data.dtypes


# In[8]:


# Check missing values in each column of training data
data.isnull().sum()


# In[9]:


df.info()


# In[10]:


#scatter_size_weight
plt.figure(figsize=(10, 6))
sns.scatterplot(df,x='Size',y='Weight' , hue = df["Quality"])
plt.title('scatter plot of size,weight')
plt.xlabel('Size')
plt.ylabel('Weight')

plt.show()


# In[11]:


#HISTOGRAM_GRAPH_OF_SWEETNESS
plt.figure(figsize=(10, 6))
sns.histplot(df,x='Sweetness' , hue = df["Quality"])
plt.title('histplot of sweetness')
plt.show()


# In[18]:


df=df.iloc[0:4001,:]
df


# In[13]:


cols=['Size', 'Weight', 'Sweetness', 'Crunchiness', 'Juiciness',
       'Ripeness', 'Acidity']


# In[17]:


#HEATMAP
sns.heatmap(df[cols].corr(),annot=True)
plt.show()


# In[ ]:




