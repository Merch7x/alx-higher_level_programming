#!/usr/bin/node
const argv = process.argv;

function add (a, b) {
  const res = a + b;
  console.log(res);
}

add(Number(argv[2]), Number(argv[3]));
