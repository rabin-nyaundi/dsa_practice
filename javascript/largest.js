//  get the largest and second largest element in arrays

function getLargest(arr) { 
    let largest = arr[0]

    if (arr.length == 0) {
        return 0
    }
    
    for (i = 1; i <= arr.length - 1; i++){
        if (arr[i] > largest) {
            largest = arr[i]
        } 
    }

    return largest

}


function getSecondLargestElement(arr) {
    let largest = arr[0]
    let secondLargest = - Infinity 
    
    for (i = 1; i <= arr.length - 1; i++){
        if (arr[i] > largest) {
            secondLargest = largest
            largest = arr[i]
        } else if (arr[i] < largest && arr[i] > secondLargest) {
            secondLargest = arr[i]
        }
    }

    return secondLargest
}


console.log(getLargest([1, 2, 3, 4, 5, 6, 10, 1]))
console.log(getSecondLargestElement([1, 2, 3, 4, 5, 6, 10, 9, 0]));

// time complexity 0(n)
// space complexity 0(1)