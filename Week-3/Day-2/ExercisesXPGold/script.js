// Exercise 1 : Favorite Color
// Instructions
// let sentence = ["my","favorite","color","is","blue"];
// Write some simple Javascript code that will join all the items in the array above, and console.log the result.

let sentence = ["my","favorite","color","is","blue"];
console.log(sentence.join(' '))

// Exercise 2 : Mixup
// Instructions
// Create 2 variables. The values should be strings. For example:
// let str1 = "mix";
// let str2 = "pod";


// 2. Slice out and swap the first 2 characters of the two strings from part 1.


// 3. Create a third variable where the value is the concatenation of the two strings from the part 1 (separated by a space).


// 4. Finally console.log the new concatenated string.



// Some Examples

// let str1 = "mix";
// let str2 = "pod";
// let newWord should be equal to 'pox mid'

// let firstWord = "Hello";
// let secondWord = "World";
// let thirdWord should be equal to 'Wollo Herld'

let str1 = "mix";
let str2 = "pod";
let str3 = str1.slice(0,2) + str2[2];
let str4 = str2.slice(0,2) + str1[2];
let str5 = str4.concat(' ', str3);
console.log(str5);

// Exercise 3 : Calculator
// Instructions
// Make a Calculator. Follow the instructions:

// Prompt the user for the first number.
// Store the first number in a variable called num1.
// Hint : console.log the type of the variable num1. What should you do to convert it to a number ?
// Prompt the user for the second number.
// Store the second number in a variable called num2.
// Create an Alert where the value is the SUM of num1 and num2.
// BONUS: Make a program that can subtract, multiply, and also divide!

let num1 = prompt("Enter a number!");
num1 = +num1;
let num2 = prompt("Enter a second number!")
num2 = +num2;
let operator = prompt("Please enter the kind of calculation you would like(+,-,*,/)")
if(operator == "+"){
    alert(num1 + num2)
} else if(operator == "-"){
    alert(num1 - num2)
}else if(operator == "*"){
    alert(num1 * num2)
} else if(operator == "/"){
    alert(num1 / num2)
} else{
    alert("Please retry and enter an appropriate operator")
}