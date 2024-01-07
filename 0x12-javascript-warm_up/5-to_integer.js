#!/usr/bin/node
const firstArg = process.argv[2];
const convertedNumber = parseInt(firstArg);

if (!isNaN(convertedNumber)) {
  console.log(`My number: ${convertedNumber}`);
} else {
  console.log('Not a number');
}
