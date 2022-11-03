def main(list1,k,n):
    
    s=0
    while k<n:
        if list1[k]%2==1:
          s+=list1[k]
        k+=1
    return s
print(main([1,2,3,4,5],0,4))
