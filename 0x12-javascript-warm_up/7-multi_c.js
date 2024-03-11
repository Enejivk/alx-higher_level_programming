#!/usr/bin/node

const numberTimes = Number(process.argv[2]);
if (isNaN(numberTimes)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numberTimes; i++) {
    console.log('C is fun');
  }
}
