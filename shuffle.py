# -*- coding: utf-8 -*-
"""
Created on Thu May  6 11:10:46 2021

@author: Salehin
"""
def shuffle(nums,n):
   final=[]
   k=n
   for i in range(n):
       final.append(nums[i])
       final.append(nums[k])
       k=k+1
   return final    


if __name__ == "__main__":
    A=[2,3,5,4,1,7]
    B=shuffle(A,3)
       
       