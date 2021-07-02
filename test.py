# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 17:59:52 2021

@author: sharukh
"""

from model import Recommendation
recommend = Recommendation()
u='00sab00'
r=recommend.getTopProducts(u)
print(r)