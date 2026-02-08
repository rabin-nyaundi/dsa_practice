package main

func twoSum(nums []int, target int) []int {
	numMap := make(map[int]int)

	for i := 0; i < len(nums); i++ {
		compliment := target - nums[i]
		if idx, ok := numMap[compliment]; ok {
			return []int{idx, i}
		}
		numMap[nums[i]] = i
	}
	return []int{}
}