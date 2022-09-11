
def binary_search_iterative(arr,n,x):
    '''
    arr -> Array(sorted) to be searched
    n -> Length of the array
    x -> Value to search
    '''
    lower=0
    upper=n
    while lower<=upper:
        mid=(lower+upper)//2
        if arr[mid]==x:
            return mid
        elif x<arr[mid]:
            upper=mid-1
        else:
            lower=mid+1
    else:
        return -1

def binary_search_recursive(arr,x,lower,upper):
    if lower>upper:
        return -1
    mid=(lower+upper)//2
    mid_ele=arr[mid]
    if mid_ele==x:
        return mid
    if mid_ele<x:
        return binary_search_recursive(arr,x,mid+1,upper)
    return binary_search_recursive(arr,x,lower,mid-1)


arr=[12,14,24,26,45,47,49,67,69,72,75,87,92,97]
x=72
lower=0
upper=len(arr)-1
print(binary_search_recursive(arr,x,lower,upper))

    


        