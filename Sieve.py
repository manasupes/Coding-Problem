#!/usr/bin/env python
# coding: utf-8

# In[9]:


def Sieve_of_Erat(n):
    not_prime = []
    for i in range(2, n+1):
        if i not in not_prime:
            print(i)
            for j in range(i*i, n+1, i):
                not_prime.append(j)

x = int(input("Enter the threshold"))
Sieve_of_Erat(x)
        


# In[ ]:


Time complexity : O(n.loglogn)

