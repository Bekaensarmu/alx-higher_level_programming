#!/usr/bin/node
// prints two arguments passed to it, in the following format: “ is ”

const newArgs = process.argv.slice(2);
if (isNaN(newArgs[0]) === false) {
  const n = parseInt(newArgs[0]);
  console.log('My number: ' + n);
} else {
  console.log('Not a number');
}
