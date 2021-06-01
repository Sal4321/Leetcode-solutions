# -*- coding: utf-8 -*-
"""
Created on Fri May 28 11:24:35 2021

@author: Salehin
"""
def checkArithmeticSubarrays(nums, l, r):
    output=[]
    lsize=len(l)
    for i in range(lsize):
        first=l[i]
        last=r[i]
        sub=nums[first:last+1]
        sub.sort()
        diff=sub[1]-sub[0]
        flag=True
        for j in range(len(sub)-1):
            if(sub[j+1]-sub[j]!=diff):
                flag=False
                break
        output.append(flag)    
    return output  
if __name__ == "__main__":
    nums = [4,6,5,9,3,7]
    l = [0,0,2]
    r = [2,3,5]
    print(checkArithmeticSubarrays(nums, l, r)) 
                    
                    