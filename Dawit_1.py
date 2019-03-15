#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Dawit Reda
#ID#10189420
#Module 1 Assignment
#Programming for the Data Science
#Submitted to Dr. Daniel Wu


# In[11]:


#quesion 1.1 the function arthimethic_opration will estimate the simple opration below and return d 
def arthimethic_opration(a,b,c):
    d= (a*b)/(b+c)
    return d

#let's pass the number 5,6,4 to the function to estimate the result
print(arthimethic_opration(5,6,4))

#output 3.0


# In[12]:


#quesion 1.2 let's create a function that retun the result as below
def sqrt_opration(x,y,z):
    #let's import math to calculate the sqayre root 
    import math
    result = (math.sqrt(x+y)) + z
    
    return result

#let's pass the value of x y z to the function and print it out
print(sqrt_opration(17,8,6))
#output 11.0


# In[13]:


#quesion 1.3 
def nth_sqrt_opration(y1,y2):
    #let's import math to calculate the nth sqayre root 
    import math
    output = (y1 - y2)**3
    
    return output

#let's pass the value of y1 and y2 to the function
print(nth_sqrt_opration(5,8))
#output -27


# In[14]:


#question 1.4 let's define a function that return a 4th square root for a variable
def forth_square_root(n, r =4):
    return n**(1/r)

#let's pass the n value(the sum of the two number from the quesion 1.4) to the function
print(forth_square_root(-21+102))
#output 3.0


# In[15]:


#question 1.5 The function below estimates the % (modulo) operator, it  yields the remainder from the division of the 
#first argument by the second.

def modulu(mod1,mod2):
    return mod1%mod2

#let's pass mod1 and mod2 value to the function
print(modulu(8,5))
#output 3


# In[ ]:




