#!/usr/bin/node

let Count = 0;

exports.logMe = function (item) {
  console.log(Count + ': ' + item);
  Count++;
};
