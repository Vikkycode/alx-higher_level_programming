#!/usr/bin/node
const count = Math.floor(Number(process.argv[2]));
console.log(isNaN(count) ? 'Not a number' : 'My number: ' + count);
