#!/usr/bin/node

const request = require('request');
const fs = require('fs');

if (process.argv.length !== 4) {
  console.error('Usage: ./5-request_store.js <url> <output_file>');
  process.exit(1);
}

const url = process.argv[2];
const outputFile = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error.message);
  } else if (response.statusCode === 200) {
    fs.writeFileSync(outputFile, body, 'utf-8');
  } else {
    console.error(`Failed to retrieve content. Status code: ${response.statusCode}`);
  }
});
