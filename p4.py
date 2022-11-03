def main(list1):
  i=0
  a=len(list1)
  s=0
  while i<a:
    if list1[i]%2==0:
        s+=list1[i]
    i+=1
  return s
print(main([5,3,2,8,5]))