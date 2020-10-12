#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing dataset first in python
import json


# In[2]:


#opening and looking
with open('data.json') as d:
    data = json.load(d)


# In[8]:


#print((data))


# In[9]:


#importing mongoclient to work with mongo
from pymongo import MongoClient


# In[10]:


#establishing cnxxtn
client = MongoClient('mongodb+srv://Joy:123@cluster0.9vh6s.gcp.mongodb.net/<data>?retryWrites=true&w=majority')

#mongodb+srv://GDuser:GDuser@cluster0.fifzk.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority
# In[11]:


#naming the database as data1
db = client.data1


# In[12]:


#creating collection named products in db
products =db.products


# In[14]:


#insrting the data imported to collection 
products.insert_many(data)


# In[ ]:
