# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:01:28 2023

@author: Balasubramaniam
"""
# Python program to implement Two Sample Z-Test   
  
# Importing the required libraries  
import pandas as pd  
from scipy import stats  
from statsmodels.stats import weightstats as stests  
  
# Creating a dataset  
data1 = [83, 85, 86, 90, 90, 93, 93, 95, 97, 97,  
         106, 108, 106, 108, 111, 113, 113, 112, 116, 111]  
  
data2 = [92, 92, 90, 93, 93, 97, 94, 98, 109, 108,  
         110, 117, 110, 115, 114, 114, 130, 130, 149, 131]  
  
# Implementing the two-sample z-test   
z_test ,p_val = stests.ztest(data1, x2 = data2, value = 0, alternative = 'two-sided')  
print(p_val)  
  
# taking the threshold value as 0.05 or 5%  
if p_val < 0.05:  
    print("We can reject the null hypothesis")  
else:  
    print("We can accept the null hypothesis")  