#!/usr/bin/node
const fs = require('fs');

function readAndPrintFile (filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    console.log(content);
  } catch (error) {
    console.error(error);
  }
}

if (process.argv.length !== 3) {
  console.error('Usage: ./0-readme.js<file_path>');
  process.exit(1);
}

const filePath = process.argv[2];
readAndPrintFile(filePath);
