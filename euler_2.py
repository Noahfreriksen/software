# -*- coding: utf-8 -*-
"""
Created on Mon Sep 9 12:57:17 2018

@author: Noah Freriksen
"""

n1 = 0
n2 = 1
fi = 0
n = 0
su = 0

for n in range(2, 4000000):
    
    if (n<=1):
        fi = n
    else:
        fi = n1 + n2
        n1 = n2
        n2 = fi
        
    if (fi%2 == 0):
        su += fi
        
print (su)
    

    
    