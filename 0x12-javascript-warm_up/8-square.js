#!/usr/bin/node
const argv = process.argv[2];
const letter = 'X';

if (!argv) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argv; i++) {
    for (let j = 0; j < argv; j++) {
      process.stdout.write(letter);
    }
    console.log();
  }
}
