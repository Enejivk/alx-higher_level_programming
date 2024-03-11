#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}
const Number1 = Number(process.argv[2]);
const Number2 = Number(process.argv[3]);
if (isNaN(Number1, Number2)) {
  console.log(Number2);
} else {
  add(Number1, Number2);
}
