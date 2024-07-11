/*
    Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).
    The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

    Mind the input validation.
*/

export function sumArray(array:number[] | null) : number {
  console.log(`\nOriginal Array: [${array}]`)
  
  if (!array || array.length === 1) {
    return 0;
  }

  // Order list
  array?.sort((a, b) => a - b)
  console.log(`Sorted Array: [${array}]`)
  
  // Remove last and first elements
  array.pop()
  array.shift()
  console.log(`Array without first and last element: [${array}]`)

  // Sum the rest of elements
  let sum: number = 0;
  array.map((item: number) => {
    sum += item;
  })
  console.log(`sum: ${sum}\n`);
  return sum;
}

export function sumArrayV2(array: number[] | null): number {
    console.log(`\nOriginal Array: [${array}]`);

    if (!array || array.length <= 2) {
        return 0;
    }

    const sortedArray = array.slice().sort((a, b) => a - b);
    console.log(`Sorted Array: [${sortedArray}]`);

    const sum = sortedArray.slice(1, -1).reduce((acc, curr) => acc + curr, 0);
    console.log(`sum: ${sum}\n`);

    return sum;
}

export function sumArrayV3(array: number[] | null): number {
    console.log(`\nOriginal Array: [${array}]`)

    if (!array || array.length <= 2) {
        return 0;
    }

    const sortedArray = array.slice().sort((a, b) => a - b);
    console.log(`Sorted Array: [${sortedArray}]`);

    let sum: number = 0;
    for (let i = 1; i < sortedArray.length - 1; i++) {
        sum += sortedArray[i];
    }
    console.log(`sum: ${sum}\n`);

    return sum;
}

export function sumArrayV4(array: number[] | null): number {
    console.log(`\nOriginal Array: [${array}]`);

    if (!array || array.length <= 2) return 0;

    // Sort the array and remove first and last element
    const sortedArray = array.sort((a, b) => a - b).slice(1, -1);
    console.log(`Sorted Array: [${sortedArray}]`);

    // Sum the rest of elements
    const sum = sortedArray.reduce((sum, currentNumber) => sum + currentNumber, 0);
    console.log(`sum: ${sum}\n`);

    return sum;
}


sumArrayV4([6, 2, 1, 8, 10])
sumArrayV4([1, 1, 11, 2, 3])
console.log(sumArray([1]))