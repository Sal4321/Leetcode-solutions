# -*- coding: utf-8 -*-
"""
Created on Thu May 27 10:05:09 2021

@author: Salehin
"""
def diagonalSum(mat):
        n=len(mat)
        i=0
        j=0
        k=i
        l=n-1-(i)
        total=0
        while i<n and j<n:
            if i==k and j==l:
                total=total+mat[i][j]
            else:
                total=total+mat[i][j]+mat[k][l]
            i=i+1
            j=j+1
            k=k+1
            l=l-1
        return total 
    
if __name__ == "__main__":
    mat=[[1,2,3],[4,5,6],[7,8,9]]
    print(diagonalSum(mat))