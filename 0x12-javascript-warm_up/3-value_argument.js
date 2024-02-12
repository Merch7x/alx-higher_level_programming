#!/usr/bin/node
const argv = process.argv;

if (!argv[2]) {
  console.log('No argument');
} else {
  for (let i = 2; i < process.argv.length; i++) {
    console.log(argv[i]);
  }
}
