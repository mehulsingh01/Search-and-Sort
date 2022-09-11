def mergeSort(arr):
    '''
    arr-> Array to be sorted
    Keeps dividing the array into two halves from the middle until the lists are atomic, 
    then keeps merging the lists in a sorted manner
    '''
    def merge_list(left,right,arr):
        '''
        left-> first half
        right-> second half
        arr-> original list
        '''
        n=len(left)
        m=len(right)
        i=j=k=0
        while True:
            if i==n:
                arr[k:k+(m-j)]=right[j:]
                break
            if j==m:
                arr[k:k+(n-i)]=left[i:]
                break
            
            elif left[i]>right[j]:
                arr[k]=right[j]
                j+=1
                k+=1
            else:
                arr[k]=left[i]
                i+=1
                k+=1    

    if len(arr)==1: #array with a single element is sorted on its own
        return 

    mid=(len(arr))//2

    left=arr[:mid]
    right=arr[mid:]    

    mergeSort(left)
    mergeSort(right)

    merge_list(left,right,arr)


arr=[4,3,5,4,2,4,4,5,6,7,6,5,4,6,7,8,6,4,2]
n=len(arr)
mergeSort(arr)
print(*arr)





