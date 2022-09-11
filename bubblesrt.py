def bubble_sort(arr,n):
    '''
    arr -> Array to be sorted
    n -> Length of the array
    Sorts in pairs
    Sorts backwards (maximum elements first)
    '''
    for i in range(n-1): # only the no' of passes, n-1 because by 2nd last iteration, all elements will be sorted from index 1 to n
        for j in range(n-i-1): # we keep decreasing the range because the array keeps getting sorted from the back
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
