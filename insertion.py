a=[10,23,5,4,99,47]
for i in range(1,len(a)):
    j=i-1;
    temp=a[i]
    while temp<a[j] and j>=0:
        a[j+1]=a[j]
        j=j-1
    j=j+1
    a[j]=temp
print("sorted array")
for i in range(len(a)):    
    print("%d" %a[i]) 