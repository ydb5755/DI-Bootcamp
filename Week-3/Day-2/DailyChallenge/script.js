// Exercise 1:
// Using this array :

// const fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
// Remove Banana from the array.
// Sort the array in alphabetical order.
// Add “Kiwi” to the end of the array.
// Remove “Apples” from the array. Don’t use the same method as in part 1.
// Sort the array in reverse order. (Not alphabetical, but reverse the current Array i.e. [‘a’, ‘c’, ‘b’] becomes [‘b’, ‘c’, ‘a’])
// At the end you should see this outcome:
// ["Kiwi", "Oranges", "Blueberries"]

const fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
fruits.shift();
fruits.sort();
fruits.push("Kiwi");
fruits.splice(0,1);
fruits.reverse();
console.log(fruits);

// Exercise 2:
// Using this array :

// const moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
// Access and then console.log “Oranges”.

const moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1][1]);