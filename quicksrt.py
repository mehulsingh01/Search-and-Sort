def quick_sort(arr, start, end):
    
    def find_pivot_point(arr,start,end):
        '''
        returns the pivot point and shallow sorts the array
        '''
        def shallow_sort_around_pivot(arr, start, end, pivot_point):
            '''
            Places elements smaller than pivot point on the left and elements greater on the right
            '''
            i=start
            j=end-1
            while True:
                for k in range(start,pivot_point):
                    if arr[k]>=arr[pivot_point]:
                        i=k
                        break
                else:
                    break
                for k in range(end-1,pivot_point,-1):
                    if arr[k]<arr[pivot_point]:
                        j=k 
                        break
                else:
                    break
                arr[i],arr[j]=arr[j],arr[i]
            
        pivot_point=0
        for i in arr[start:end]:
            if i < arr[start]:
                pivot_point+=1
        pivot_point+=start
        #move pivot point to the right position
        arr[start],arr[pivot_point]=arr[pivot_point],arr[start]
        shallow_sort_around_pivot(arr, start, end, pivot_point) 
        return pivot_point

    if start>=end:
        return
    pivot_point=find_pivot_point(arr,start,end)

    quick_sort(arr,start,pivot_point)

    quick_sort(arr,pivot_point+1,end)
    
arr=[]
quick_sort(arr,0,len(arr))
print(arr)

        
            
            