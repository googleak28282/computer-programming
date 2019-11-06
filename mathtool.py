# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 15:00:37 2019

@author: user
"""
def euler(dy,x0,y0,xs):
    ans=[]
    ans.append(y0)
    for i in range(1,len(xs)):
   #     print(i)
#        print(ans[i-1])
    #    print(xs[i])
        print((ans[i-1])+(xs[i]-xs[i-1])*dy(ans[i-1]))
        ans.append((ans[i-1])+(xs[i]-xs[i-1])*dy(ans[i-1]))
    return ans
