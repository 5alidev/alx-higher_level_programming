#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arr = process.argv.slice(2).map(Number);
  const max = Math.max(...arr);
  const index = arr.indexOf(max);
  arr.splice(index, 1);
  const secondMax = Math.max(...arr);
  console.log(secondMax);
}
