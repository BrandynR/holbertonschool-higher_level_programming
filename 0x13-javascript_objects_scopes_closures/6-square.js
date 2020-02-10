#!/usr/bin/node

const square = require('./5-square.js');
module.exports = class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let c_wide = '';
    for (let i = 0; i < this.height; i++) {
      c_wide = '';
      for (let j = 0; j < this.width; j++) {
        c_wide += c;
      }
      console.log(c_wide);
    }
  }
};
