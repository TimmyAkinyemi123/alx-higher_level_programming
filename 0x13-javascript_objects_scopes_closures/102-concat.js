#!/usr/bin/node
const fs = require('fs');
const [,, fileA, fileB, fileC] = process.argv;

/**
 * read contents of first source file
 */
const contentA = fs.readFileSync(fileA, 'utf-8');

/**
 * read contmets if the second source file
 */
const contentB = fs.readFileSync(fileB, 'utf-8');

/**
 * concatenate the contents
 */
const contentAB = contentA + contentB;

/**
 * write to destination file
 */
fs.writeFileSync(fileC, contentAB);
