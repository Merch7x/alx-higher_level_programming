#!/usr/bin/node
const argv = process.argv[2];
const letter = 'X';

if (!argv) {
  console.log('Missing size');
} else if (argv <= 0) {
  process.exit();
} else {
  for (let i = 0; i < argv; i++) {
    let row = '';
    for (let j = 0; j < argv; j++) {
      row += letter;
    }
    console.log(row);
  }
}
