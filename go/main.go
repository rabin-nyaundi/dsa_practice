package main

import "fmt"

func main() {
	marks := []int{1, 2, 4, 7, 0, 105, 999, 10001}

	fmt.Println(getLargestElement(marks))
	fmt.Println(twoSum(marks, 9))
}
