def main(list1):
    i=0
    a=len(list1)
    s=0
    while i<a:
        s+=int(list1[i])
        i+=1
    return s
print(main([6,3,1]))


