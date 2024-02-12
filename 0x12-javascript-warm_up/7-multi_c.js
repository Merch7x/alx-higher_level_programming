#!/usr/bin/node
let argv = process.argv[2];

const myVar = 'C is fun';

if (!argv) {
  console.log('Missing number of occurrence');
} else if (argv <= 0) {
  process.exit();
} else {
  while (argv) {
    console.log(myVar);
    argv = argv - 1;
  }
}
