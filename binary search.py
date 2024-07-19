#list=[1,2,3,8,9,10]
#first=0
#last=len(list)-1
"""def binarysearch(list,ele):
    first=0
    last=len(list)
    print(last)
    mid=0
    while first<=last:
        mid=(first+last)//2
        if ele==list[mid]:
            return mid
        elif list[mid]<ele:
           first=mid+1
        elif list[mid]>ele:
           last=mid-1
    else:
        return -1
    
result=binarysearch([1,2,3,8,9,10],8)
if result!=-1:
    print("found")
else:
    print("not found")"""
    
def binarysearch(list,ele):
    low=0
    high=len(list)
    mid=0
    while low<=high:
        mid=(low+high)//2
        if  ele==list[mid]:
            return mid
        elif ele>list[mid]:
            low=mid+1
        elif ele<list[mid]:
            high=mid-1
        else:
            return -1
resuli=binarysearch([1,2,3,8,9,10],8)
if resuli!=-1:
    print(" found")
else:
    print("not found")
            
    
