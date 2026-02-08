function twoSum(nums, target) {
  const numsMap = new Map();
  for (let i = 0; i < nums.length; i++) {
    const compliment = target - nums[i];
    if (numsMap.has(compliment)) {
      return [numsMap.get(compliment), i];
    }
    numsMap.set(nums[i], i);
  }
  return [];
}

numbers = [1, 2, 3, 99, 4, 101, 0, 5, 6, 9, 3];
console.log(twoSum(numbers, 9));
