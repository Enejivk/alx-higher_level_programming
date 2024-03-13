#!/usr/bin/node

const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size, w, h) {
    super(size, size);
  }
}

module.exports = Square;
