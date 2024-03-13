#!/usr/bin/node

const oldSquare = require('./5-square');
class Square extends oldSquare {
  charPrint (c) {
    let star = '';
    let char;
    if (c) {
      char = c;
    } else {
      char = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      star += char;
    }
    for (let j = 0; j < this.height; j++) {
      console.log(star);
    }
  }
}

module.exports = Square;
