#!/usr/bin/node

const numberTimes = Number(process.argv[2]);
if (isNaN(numberTimes)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < numberTimes; i++) {
    let row = '';
    for (let j = 0; j < numberTimes; j++) {
      row += 'x';
    }
    console.log(row);
  }
}
