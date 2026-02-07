package main

import (
	"fmt"
	"math"
)

func main(){
	marks := []int{1, 2, 4, 7, 0, 105, 999, 10001}

	fmt.Println(getLargestElement(marks))
}


func getLargestElement(arr []int) (int, float64){
	largest := arr[0]
	secondLargest := math.Inf(-1)

	for i := 0; i <= len(arr) -1; i++ {
		if arr[i] > largest {
			secondLargest = float64(largest)
			largest = arr[i]
		}
	}

	return largest, secondLargest
}