




def binary_search_iteration_methode(arr, element):
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

def binary_search_recursive_methode(arr, element, high, low):
    mid = (low + high) // 2
    while low<= high:
        if element == arr[mid]:
            return mid
        elif element > arr[mid]:
            return binary_search_recursive_methode(arr, element, high, low = mid + 1)    
        else:
            return binary_search_recursive_methode(arr, element, high = mid - 1, low = low)   
        
    return 'Not found'       
arr = [1,2,3,4,5,6,7,8,9,22,423,434,554,666]


x = 22
print(binary_search_iteration_methode(arr,x))
print( binary_search_recursive_methode(arr, x, len(arr)-1, 0))


