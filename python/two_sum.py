
def two_sum(nums:list, target: int) -> int:
    num_map: dict = {}
    for i, num in enumerate(nums):
        print(enumerate(nums))
        compliment = target - num
        if compliment in num_map:
            return [num_map[compliment], i]
        num_map[num] = i
        
        
numbers = [1, 2, 3, 99, 4, 101, 0, 5, 6, 9, 3]
print(two_sum(numbers, 9))

# Time Complexity = 0(n)
# Space complexity 0(n)