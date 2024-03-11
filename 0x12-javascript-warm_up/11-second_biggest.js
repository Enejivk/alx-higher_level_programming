#!/usr/bin/node

if (process.argv.length === 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  let index = 2;
  let secondLargest = 0;
  let largest = parseInt(process.argv[index]);
  while (index < process.argv.length) {
    const currentNumber = parseInt(process.argv[index]);
    if (currentNumber > largest) {
      secondLargest = largest;
      largest = currentNumber;
    }
    if (currentNumber < largest && currentNumber > secondLargest) {
      secondLargest = currentNumber;
    }
    index++;
  }
  console.log(secondLargest);
}
