# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 21:02:40 2023

@author: Balasubramaniam
"""
# Python program to implement One-Way f-test  
  
# Importing the required libraries  
import scipy.stats  
  
# Creating sample data  
data1 = [0.0842, 0.0368, 0.0847, 0.0935, 0.0376, 0.0963, 0.0684,  
             0.0758, 0.0854, 0.0855]  
data2 = [0.0785, 0.0845, 0.0758, 0.0853, 0.0946, 0.0785, 0.0853,  
           0.0685]  
data3 = [0.0864, 0.2522, 0.0894, 0.2724, 0.0853, 0.1367, 0.853]  
  
# Performing the F-Test   
f_test, p_val = scipy.stats.f_oneway(data1, data2, data3)  
print("p-value is: ", p_val)  
  
# taking the threshold value as 0.05 or 5%  
if p_val < 0.05:      
    print(" We can reject the null hypothesis")  
else:  
    print("We can accept the null hypothesis")  