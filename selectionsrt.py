def selection_sort(arr,n):
    '''
    arr -> Array to be sorted
    n -> Length of the array
    Finds the minimum of the remaining list and swaps with position at i
    Sorts from the beginning 
    
    '''
    for i in range(n):
        min=i
        for j in range(i,n):
            if arr[min]>arr[j]:
                min=j
        arr[min],arr[i]=arr[i],arr[min]

