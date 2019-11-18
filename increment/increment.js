/*
Topics: fundamentals, closures
Create a function called incrementCounter
incrementCount leverages a closure to keep track a variable that gets incremented

Ex:
incrementCounter() //  returns 1
incrementCounter() //  returns 2
incrementCounter() //  returns 3

Solution must leverage closures, should not use global variables or object instance properties
*/

function incrementCounter() {
  let counter = 0;
  return () => {
    counter++;
    return counter;
  };
}

let counter = incrementCounter();
console.log(counter()); // return 1
console.log(counter()); // return 2
console.log(counter()); // return 3
