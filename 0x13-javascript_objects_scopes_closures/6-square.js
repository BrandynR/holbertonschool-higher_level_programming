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
    for (let i = 0; i < this.width; i++) {
      c_wide += c;
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c_wide);
    }
  }
};
