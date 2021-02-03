#!/usr/bin/node
const number = Math.floor(Number(process.argv[2]));
if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < number; i++) {
    let printX = '';
    for (let j = 0; j < number; j++) {
      printX = printX + 'X';
    }
    console.log(printX);
  }
}
