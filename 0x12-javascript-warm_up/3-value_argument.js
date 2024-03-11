#!/usr/bin/node
const count = process.argv[2];
console.log(typeof count === 'undefined' ? 'No argument' : count);
