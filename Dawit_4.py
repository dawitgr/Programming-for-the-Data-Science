#!/usr/bin/env python
# coding: utf-8

# In[15]:


"""
Dawit Reda
ID#10189420
Module 4 Assignment
Programming for the Data Science
Submitted to Dr. Daniel Wu
"""


# In[25]:


#4.1 Given three lists: list_1 = [1,2,3,4,16], list_2=["1","2","3","4","F"], and list_3= ["PA","NJ"]
#import pandas
import pandas as pd
#Given lists
list_1 = [1,2,3,4,16]
list_2=['1','2','3','4','F']
list_3= ['PA','NJ']


# In[27]:


#4.2 Create a data frame using pandas package and the above lists so that list_1 and list_2 are indexed by list_3
#zip the list_1 and list_2
df_zip = pd.DataFrame(list(zip(list_1, list_2)))

#convert the dataframe column into row
df=df_zip.T

#set list_3 as index to df
df = df.set_index([list_3])
df


# In[32]:


#4.3 Multiply every value by 5 (hint: use anonymous function, i.e. lamda function: 
#e.g. df.apply(lamda x: x*2) will multiply every value by 2).
#Use print function to discuss if there are problems with the results

df_mul_five =df.apply(lambda x: x*5)

#we can see that the list_2 is taking our function as a string and it is calling each string five times as below like("FFFFF")
print(df_mul_five)


# In[33]:


#4.4 Use pandas’ to_numeric method to clean up the data. (Note: you may have to use the optional errors argument
#Convert all arguments to a numeric type using to_numeric
df_converted = df.apply(pd.to_numeric,errors='coerce')

#the string(variable values of the list_2 becomes numeric and the "F value becomes a NAN ==> not a number"
df_converted


# In[34]:


#4.5 Now try again to multiply all the values by 5.
#use lambda expression to muliply all the vallues by 5 to the new cleaned value
df_multiply_five =df_converted.apply(lambda x: x*5)
#the value becomes irent after the string(var) values converted into numeric 
df_multiply_five


# In[ ]:




