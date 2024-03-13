#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let star = '';
    for (let i = 0; i < this.width; i++) {
      star += 'x';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(star);
    }
  }
}
module.exports = Rectangle;
