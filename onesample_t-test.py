# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 20:51:32 2023

@author: Balasubramaniam
"""
# Python program to implement T-Test on a sample of ages  
  
# Importing the required libraries  
from scipy.stats import ttest_1samp  
import numpy as np  
  
# Creating a sample of ages  
ages = [45, 89, 23, 46, 12, 69, 45, 24, 34, 67]  
print(ages)  
  
# Calculating the mean of the sample  
mean = np.mean(ages)  
print(mean)  
  
# Performing the T-Test   
t_test, p_val = ttest_1samp(ages, 30)  
print("P-value is: ", p_val)  
  
# taking the threshold value as 0.05 or 5%  
if p_val < 0.05:      
    print(" We can reject the null hypothesis")  
else:  
    print("We can accept the null hypothesis")  