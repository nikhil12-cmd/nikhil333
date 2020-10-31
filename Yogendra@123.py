#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup


# In[2]:


import requests


# In[3]:


url="https://getpython.wordpress.com/"


# In[4]:


source=requests.get(url)


# In[5]:


soup=BeautifulSoup(source.text,'html')


# In[6]:


title=soup.find('title')


# In[7]:


print("this is with html tags :",title)


# In[8]:


qwery=soup.find('h1')


# In[9]:


print("this is without html tags:",qwery.text) 


# In[10]:


links=soup.find('a')


# In[11]:


print(links)


# In[12]:


print(links['href'])


# In[13]:


print(links['class'])


# In[14]:


many_link=soup.find_all('a')
total_links=len(many_link)
print("total links in my website :",total_links)
print()
for i in many_link[:6]:
    print(i)


# In[16]:


second_link=many_link[1]
print(second_link)
print()
print("href is :",second_link['href'])


# In[17]:


nested_div=second_link.find('div')
print(nested_div)
print()
z=(nested_div['class'])
print(z)
print(type(z))
print()
print("class name of div is :"," ".join(nested_div['class']))


# In[18]:


wiki=requests.get("https://en.wikipedia.org/wiki/World_War_II")
soup=BeautifulSoup(wiki.text,'html')
print(soup.find('title'))


# In[19]:


ww2_contents=soup.find_all("div",class_='toc')
for i in ww2_contents:
    print(i.text)


# In[ ]:




