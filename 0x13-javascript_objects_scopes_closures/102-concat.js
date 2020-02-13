#!/usr/bin/node

const fs = require('fs');
const src1 = process.argv[2];
const src2 = process.argv[3];
const dest = process.argv[4];

fs.readFile(src1, 'utf8', (err, data) => {
  if (err) console.log(err);
  else {
    fs.appendFile(dest, data, 'utf8', (err) => {
      if (err) console.log(err);
    });
  }
});

fs.readFile(src2, 'utf8', (err, data) => {
  if (err) console.log(err);
  else {
    fs.appendFile(dest, data, 'utf8', (err) => {
      if (err) console.log(err);
    });
  }
});
