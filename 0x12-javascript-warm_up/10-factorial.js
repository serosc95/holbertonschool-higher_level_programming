#!/usr/bin/node
const number = Math.floor(Number(process.argv[2]));
console.log(factorial(number));

function factorial (number) {
  if (number === 0 || isNaN(number)) {
    return (1);
  }
  return (number * factorial(number - 1));
}
