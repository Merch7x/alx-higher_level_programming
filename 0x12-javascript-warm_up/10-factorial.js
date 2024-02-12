#!/usr/bin/node
const argv = process.argv[2];

function factorial (x) {
  if (x < 0) {
    return undefined;
  }
  let result = 1;
  for (let i = 2; i <= x; i++) {
    result *= i;
  }
  return result;
}

console.log(factorial(argv));
