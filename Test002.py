
# coding: utf-8

# In[1]:


#Yuan Fang 111572616

get_ipython().magic('matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interpolate

def func(x):
    return 3*x*np.log(x)-np.exp(-(36*x-36/np.e)**4)/36

grid_x, grid_y = np.mgrid[-0.5:1.5:100j, -0.6:0.4:100j]
x = np.linspace(-0.5,1,100)

fig = plt.figure()
plt.plot(func(x),x)
plt.ylim(0,1)
plt.xlim(-2.2,0.2)
ax = plt.gca()
plt.text(-1.5,0.35 , r"nipple")


