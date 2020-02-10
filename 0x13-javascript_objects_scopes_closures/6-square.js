#!/usr/bin/node

const square = require('./5-square.js');
module.exports = class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    const array = [];
    for (let i = 0; i < this.width; i++) {
      array.push(c);
    }
    for (let i = 0; i < this.height; i++) {
      console.log(array.join(''));
    }
  }
};
