#!/usr/bin/node

const num = parseInt(process.argv[2]);
function factorial (a) {
  if (!a) {
    return (1);
  }
  return (a * factorial(a - 1));
}
console.log(factorial(num));
