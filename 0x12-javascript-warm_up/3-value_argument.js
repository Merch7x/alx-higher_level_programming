#!/usr/bin/node
const argv = process.argv;

if (!argv[2]) {
  console.log('No argument');
}

for (const arg of argv.slice(2)) {
  console.log(arg);
}
