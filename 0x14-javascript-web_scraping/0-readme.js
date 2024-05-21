#!/usr/bin/node

const fs = require('fs');

const fileName = process.argv[2];
fs.readFile(fileName, (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  console.log(data.toString());
});
