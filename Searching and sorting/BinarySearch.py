




def binary_search(arr, element):
    high = len(arr)-1
    low = 0
    iterations = 0
    
    while low <= high:
        mid = (low + high) // 2
        iterations += 1
        if element == arr[mid]:  
            return mid
        elif element < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1           
    return 'Not found'
            
arr = [1,2,3,4,5,6,7,8,9,22,423,434,554,666]


x = 552
print(binary_search(arr,x))


