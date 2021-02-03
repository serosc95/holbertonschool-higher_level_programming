#!/usr/bin/node
const number1 = Math.floor(Number(process.argv[2]));
const number2 = Math.floor(Number(process.argv[3]));
console.log(add(number1, number2));

function add (a, b) {
  return (a + b);
}
