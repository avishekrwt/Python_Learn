/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */

export function cookingStatus(timer) {
  if (timer == undefined){
    return 'You forgot to set the timer.';
  }
  else if (timer==0) {
    return 'Lasagna is done.';
  } 
  return 'Not done, please wait.';
}

export function preparationTime(layers,time) {
  let actualTime = time ?? 2;
  return layers.length * actualTime;
}

export function quantities(layers) {
  let noodles = layers.filter(item => item == 'noodles').length;
  let sauce = layers.filter(item => item == 'sauce').length;
  let noodlesauce = {
    noodles : noodles*50,
    sauce : sauce*0.2
  };
  return noodlesauce
}

export function addSecretIngredient(friendsList,myList) {
  let last = friendsList.length;
  let secret = friendsList[last-1];
  myList.push(secret);
}

export function scaleRecipe(recipe, portion) {
  const factor = portion / 2;
  const scaledRecipe = {};

  for (const ingredient in recipe) {
    scaledRecipe[ingredient] = recipe[ingredient] * factor;
  }

  return scaledRecipe;
}