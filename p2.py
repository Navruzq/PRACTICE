def main(list1):
        

    i=0
    a=len(list1)
    s=0
    while i<a:
        if i%2==0:
           s+=list1[i]
        i+=1
    return s
print(main([7,1,5,2,8])) 