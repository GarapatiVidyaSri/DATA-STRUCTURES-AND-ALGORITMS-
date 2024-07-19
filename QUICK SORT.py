print("--------------------QUICK SORT-----------------")
def partition(array,low,high):
    pivot=array[high]
    i=low-1
    for j in range(low,high):
        if array[j]<=pivot:
            i+=1
            array[i],array[j]=array[j],array[i]
    array[i+1],array[high]=array[high],array[i+1]
    return i+1
def quicksort(array,low,high):
    if low<high:
        pi=partition(array,low,high)
        quicksort(array,low,pi-1)
        quicksort(array,pi+1,high)
array=[10,80,9,1,87878,45,32]
quicksort(array,0,len(array)-1)
print(array)
        
