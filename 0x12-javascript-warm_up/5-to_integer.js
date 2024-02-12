#!/usr/bin/node
const argv = process.argv;

if (typeof argv[2] === 'number') {
  console.log(`My number: ${argv[2]}`);
} else if (!isNaN(argv[2])) {
  console.log(`My number: ${argv[2]}`);
} else {
  console.log('Not a number');
}
