#!/usr/bin/node

const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size, w, h) {
    super(w, h);
    this.width = size;
    this.height = size;
  }
}

module.exports = Square;
