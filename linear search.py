print("--------------linear search--------------")
def linearsearch(list,ele):
    for i in range(0,len(list)):
        if list[i]==ele:
            return i
    return -1

result=linearsearch([1,2,3,7,9,0],0)
print(result)
if result==-1:
    print("not found")
else:
    print("found")
