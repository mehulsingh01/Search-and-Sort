def join_two_lists(arr1,arr2):
    '''
    arr1 -> 1st array to be joined
    n -> Length of the arr1
    arr2 -> 2nd array to be joined
    m -> Length of arr2
    Joining two lists (sorted) in a sorted manner
    '''
    n=len(arr1)
    m=len(arr2)
    i=j=0
    arr3=[]
    while True:
        if i==n:
            arr3.extend(arr2[j:])
            return arr3
        elif j==m:
            arr3.extend(arr1[i:])
            return arr3
        elif arr1[i]<arr2[j]:
            arr3.append(arr1[i])
            i+=1
        else:
            arr3.append(arr2[j])
            j+=1
