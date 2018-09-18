# -*- coding: utf-8 -*-
"""
Created on Mon Sep 9 12:26:43 2018

@author: Noah Freriksen
"""

n = 0
su = 0

for n in range(0,999):
    
    if ((n%5==0) | (n%3==0)):
        su += n
        n += 1
        
print(su)
    
    