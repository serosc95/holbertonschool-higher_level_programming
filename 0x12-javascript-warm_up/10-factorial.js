#!/usr/bin/node
const number = Math.floor(Number(process.argv[2]));
if (isNaN(number)) {
  console.log(1);
} else {
  let factorial = 1;
  for (let i = 1; i < number + 1; i++) {
    factorial = factorial * i;
  }
  console.log(factorial);
}
