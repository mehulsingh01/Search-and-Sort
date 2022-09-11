def insertion_sort(arr,n):
    '''
    arr -> Array to be sorted
    n -> Length of the array
    The array is divided into two arrays, one assumed to be sorted (arr[0,i]) and other unsorted (arr[i,n])
    '''
    for i in range(1,n):#traverssing unsorted array
        to_swap=i
        for j in range(i-1,-1,-1):#traversing assumed sorted array
            if arr[to_swap]<arr[j]:
                arr[to_swap],arr[j]=arr[j],arr[to_swap]
                to_swap=j
        