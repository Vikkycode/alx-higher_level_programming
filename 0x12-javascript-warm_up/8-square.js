#!/usr/bin/node
const square = 'X';
const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    console.log(square.repeat(x));
  }
}
