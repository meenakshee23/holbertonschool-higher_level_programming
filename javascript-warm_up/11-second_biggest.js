#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  let max = args[0];
  let second = -Infinity;

  for (let i = 1; i < args.length; i++) {
    if (args[i] > max) {
      second = max;
      max = args[i];
    } else if (args[i] > second && args[i] < max) {
      second = args[i];
    }
  }

  console.log(second);
}
