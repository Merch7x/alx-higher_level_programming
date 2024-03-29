#!/usr/bin/node
exports.converter = function (base) {
  return function convertToBase10(number) {
    if (number < base) {
      return String(number);
    } else {
      return convertToBase10(Math.floor(number / base)) +
        String(number % base);
    }
  };
};