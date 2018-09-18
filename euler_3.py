# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 08:34:42 2018

@author: Noah Freriksen
"""

n = 600851475143
i = 2
while i * i <= n:
    if n % i:
        i += 1
    else:
        n //= i
print(n)