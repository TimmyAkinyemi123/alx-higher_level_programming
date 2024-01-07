#!/usr/bin/node

const { dict } = require('./101-data');

function invertOccurrencesDict (inputDict) {
  const resultDict = {};

  for (const userId in inputDict) {
    const occurrences = inputDict[userId];

    if (!resultDict[occurrences]) {
      resultDict[occurrences] = [];
    }
    resultDict[occurrences].push(userId.toString());
  }
  return (resultDict);
}
const invertedDict = invertOccurrencesDict(dict);

console.log(invertedDict);
