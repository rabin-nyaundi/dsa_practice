package main

import "math"

func getLargestElement(arr []int) (int, float64) {
	largest := arr[0]
	secondLargest := math.Inf(-1)

	for i := 0; i <= len(arr)-1; i++ {
		if arr[i] > largest {
			secondLargest = float64(largest)
			largest = arr[i]
		}
	}

	return largest, secondLargest
}
