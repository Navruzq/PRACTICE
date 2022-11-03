def main(list1,k,n):
    
    s=0
    while k<n:
        s+=list1[k]
        k+=1
    return s
print(main([6,2,8,1,6,3,7],2,4))
