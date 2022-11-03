def main(list1):
        

    i=0
    a=len(list1)
    s=0
    while i<a:
        if i%2==1:
           s+=list1[i]
        i+=1
    return s
print(main([7,8,3,5,2])) 