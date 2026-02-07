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


def getSecondLargest(arr: list):
    largest = arr[0]
    secondLargest = float('-inf')
    
    for num in range(len(arr)):
        if arr[num] > largest:
            secondLargest = largest
            largest = arr[num]
            
        elif arr[num] < largest and arr[num] > secondLargest:
            secondLargest = arr[num]
            
    return largest, secondLargest


marks = [11,0,3,100, 897, 888, 0,1,2,7,98]
result = print(getSecondLargest(marks))