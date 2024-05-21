#!/usr/bin/node

const fs = require('fs');

const fileName = process.argv[2];
const contentToWrite = process.argv[3];

fs.writeFile(fileName, contentToWrite, (err) => {
  if (err) {
    console.error(err);
  }
});
