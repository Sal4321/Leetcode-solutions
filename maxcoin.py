# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 19:19:37 2021

@author: Salehin
"""
def maxCoins(piles):
    piles.sort(reverse=True)
    count=0
    i=0
    j=1
    length=int(len(piles)/3)
    for i in range(length):
        count=count+piles[j]
        j=j+2
    return count    

if __name__ == "__main__":
    piles=[2,4,1,5,7,8,6,9,3]
    print(maxCoins(piles))    
    