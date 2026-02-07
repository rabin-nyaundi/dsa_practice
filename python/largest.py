def getLargestNmber(arr: list):
    largest = arr[0]
    
    if len(arr) == 0:
        return 0
    
    for num in range(len(arr)):
        if arr[num] > largest:
            largest = arr[num]
            
    return largest
            
numbers = [1, 2, 3, 99, 4, 101, 0, 5, 6, 9, 3]           
result = getLargestNmber(numbers)
print(result)