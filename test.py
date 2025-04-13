#!/usr/bin/env python
# coding: utf-8

# In[2]:


def increment(x):
    return x + 1

def test_increment():
    assert increment(3) == 4
    assert increment(5) == 6, "Increment failed"
    
    #Catch failures with try/except
    try:
        assert increment(-2) == -1 
    except AssertionError:
        print("Incrementing negative number failed")
        


# In[3]:


test_increment()


# In[7]:


def decrement(x):
    return x - 1

def test_decrement():
    assert decrement(3) == 2
    assert decrement(5) == 4
    
    try:
        assert decrement(-2) == -3
    except AssertionError:
        print("decrementing negative number failed")


# In[6]:


test_decrement()


# In[1]:


def is_positive(x)
    if (x > 0)
        return "YES"
    else
        return "NO"
    
def test_is_positive()
    assert is_positive(15) == "YES"
    assert is_positive(-11) == "NO",
    
    try:
        assert is_positive(-1111111111111111111111111) == "NO"
    except AssertionError:
        print("large numbers give error")
    


# In[ ]:




