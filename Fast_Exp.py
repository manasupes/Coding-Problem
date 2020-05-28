#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Using Recusrsive approach
def power(a, N):
    if(N==0):
        return 1;
    elif N==1:
        return a;
    else:
        R = pow(a, N/2)
        if(N%2==0):
            return R*R;
        else:
            return R*a*R;
        
a = int(input("Enter a:",))
N = int(input("Enter N:",))
power(a, N)


# In[ ]:




