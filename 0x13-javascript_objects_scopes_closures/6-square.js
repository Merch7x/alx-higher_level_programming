#!/usr/bin/node
const Rectangle = require('./5-square');
module.exports = class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      const letter = 'C';
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += letter;
        }
        console.log(row);
      }
    }
  }
};
