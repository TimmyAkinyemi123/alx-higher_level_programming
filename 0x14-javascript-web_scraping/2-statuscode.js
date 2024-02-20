#!/usr/bin/node
const axios = require('axios');

if (process.argv.length !== 3) {
  console.error('Usage: ./2-statuscode.js <URL>');
  process.exit(1);
}

const url = process.argv[2];

axios.get(url)
  .then(response => {
    console.log('code:', response.status);
  })
  .catch(error => {
    console.log('code:', error.response.status);
  });
