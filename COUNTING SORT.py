print("--------------- COUNTING SORT ---------------")
def countingSort(arr):
    size=len(arr)
    p=max(arr)
    output=[0]*size
    count=[0]*(p+1)
    for m in range(0,size):
        count[arr[m]]+=1
    for m in range(1,p+1):
        count[m]+=count[m-1]
    m=size-1
    while m>=0:
        output[count[arr[m]]-1]=arr[m]
        count[arr[m]]-=1
        m-=1
    for m in range(0,size):
        arr[m]=output[m]
data=[1,4,1,2,7,5,2]
countingSort(data)
print("SORTED ARRAY:")
print(data)
        
        
