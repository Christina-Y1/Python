#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scipy
from scipy import stats
import numpy as np

a = np.array([185, 175, 170, 169, 171, 172, 175, 157, 170, 172, 167, 173, 168, 167, 166,
              167, 169, 172, 177, 178, 165, 161, 179, 159, 164, 178, 172, 170, 173, 171])

m = stats.mode(a)
print(m)

_________________________________

import numpy as np

a = np.array([185, 175, 170, 169, 171, 172, 175, 157, 170, 172, 167, 173, 168, 167, 166,

              167, 169, 172, 177, 178, 165, 161, 179, 159, 164, 178, 172, 170, 173, 171])
m = np.median(a)
print(m)
