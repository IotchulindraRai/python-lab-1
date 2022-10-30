#!/usr/bin/env python
# coding: utf-8

# <!-- to eleborate variable and their data type such as int ,  float, boolean, string , list, set , dictionary and tuples, -->
#  

# In[1]:


#Write Python program
#a. Implement python script to show the usage of various operators available in python
#language.

a= 15 
b=2.4 
c="python Foer me" 
d=True 
e=[6,20.3,"Semester","Chulin"]
f={2,4,6,8,1,3,7,9}
g=(6,2.4,"Python","Chulin")
h={"a":6.4,"Python":"language"}
print("value of a=",a)
print("type of a=",type(a))
print("value of b=",b)
print("type of b=",type(b))
print("value of c=",c)
print("type of c=",type(c))
print("value of d=",d)
print("type of d=",type(d))
print("value of e=",e)
print("type of e=",type(e))
print("value of f=",f)
print("type of f=",type(f))
print("value of g=",g)
print("type of g=",type(g))
print("value of h=",h)
print("type of h=",type(h))


# In[1]:


# swaping two number
a=int(input("enter first nnumber"))
b=int(input("enter the second number"))
print("before swapping a=",a,"and b=",b)
a,b=b,a
print("after swapping a=",a,"and b=",b)


# In[1]:



# 1b To perform  mathematical operation such as addition ,  subtraction , multiplivation , division , module, power and also explore operator precedurce
a= int(input("enter firest number"))
b= int(input("enter second number"))

sum=a+b
sub=a-b
pro=a*b
div=a/b
rem=a%b
pow=a**b
flr = a//b
print("sum of {} and {} is : {}".format(a,b,sum))
print("subtraction of {} and {} is : {}".format(a,b,sub))
print(" product of  {} and {} is : {}".format(a,b,pro))
print("div of {} and {} is : {}".format(a,b,div))
print("reminder of {} and {} is : {}".format(a,b,rem))
print("power of {} and {} is : {}".format(a,b,pow))
print("floor division of {} and {} is : {}".format(a,b,flr))
# Prepared by chulindra


# In[5]:


# operator precedence
a=15
b=10
c=10
d=5
e=(a+b)*c/d
print("Value of (a+b)*c/d=",e)
e=((a+b)*c)/d
print("value of ((a+b)*c)/d=",e)
e=(a+b)*(c/d)
print("value of (a+b)*(c/d) =",e)
# submitted by chulindra Rai 
#usn 20BTRCO013


# In[ ]:




