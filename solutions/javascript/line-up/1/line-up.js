//
// This is only a SKELETON file for the 'Line Up' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const format = (name, number) => {
  let last = number%100;
  let rank = 'th';
  if (last%10 == 1 && last != 11) {
    rank = 'st';
  }
  else if (last%10 == 2 && last != 12) {
    rank = 'nd';
  }
  else if (last%10 == 3 && last != 13) {
    rank = 'rd';
  }
  return `${name}, you are the ${number}${rank} customer we serve today. Thank you!`
};
