#!/usr/bin/node

let i = 0;
while (process.argv[i] !== undefined) {
  i++;
}
if (i <= 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
