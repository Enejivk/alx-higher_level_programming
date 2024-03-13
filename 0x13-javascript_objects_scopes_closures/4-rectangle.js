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
      star += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(star);
    }
  }

  rotate () {
    const temp = this.width;
    this.height = this.width;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
