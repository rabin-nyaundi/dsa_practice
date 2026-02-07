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