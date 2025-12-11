#!/usr/bin/node
const nums = process.argv.slice(2).map(Number);

if (nums.length < 2) {
  console.log(0);
} else {
  let max = nums[0];
  let second = -Infinity;

  for (let i = 1; i < nums.length; i++) {
    if (nums[i] > max) {
      second = max;
      max = nums[i];
    } else if (nums[i] > second && nums[i] < max) {
      second = nums[i];
    }
  }

  console.log(second);
}
