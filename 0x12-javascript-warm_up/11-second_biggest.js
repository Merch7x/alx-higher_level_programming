#!/usr/bin/node

const args = process.argv.slice(2);

const numbers = args.map(Number);

if (numbers.length < 2) {
  console.log(0);
} else {
  numbers.sort((a, b) => b - a);

  const secondLargest = numbers[1];

  console.log(secondLargest);
}
