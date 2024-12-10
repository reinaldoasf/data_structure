def quicksort_optimized(arr,left,right):
    if left < right:
        print(arr[left:right])
        part_arr = partition(arr,left,right)
        quicksort_optimized(arr,left,part_arr-1)
        quicksort_optimized(arr,part_arr+1,right)





def partition(arr,left,right):
    pivot_index = (left+right)//2
    i = left-1
    pivot = arr[pivot_index]
    for j in range(left,right):
        if arr[j] <= pivot:
            i+=1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[pivot_index] = arr[pivot_index], arr[i+1]

    return i+1
arr = [1, 99, 123,3,66,12,-2]
quicksort_optimized(arr,0,len(arr)-1)

print(arr)