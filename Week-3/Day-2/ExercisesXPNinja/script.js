// Exercise 1 : Evaluation
// Instructions
// For each expression, predict what you think the output will be in a comment (//) without first running the command.
// Of course, explain each prediction.
// Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.

// Evaluate the comparisons found below:

// Look at this link for help

//     5 >= 1
// prediction-True because 5 is greater than 1
// Actual -True

//     0 === 1
// prediction- false because 0 does not equal 1
// actual-false

//     4 <= 1
// prediction-false because 4 is greater than, not less than 1
// actual-false

//     1 != 1
// prediction-false because 1 does in fact equal 1 and is not, not 1
// actual-false

//     "A" > "B"   
// prediction-false because in binary B is a larger number than A
// Actual-false

//     "B" < "C"
// prediction- true because binary C is greater than B
// actual-true

//     "a" > "A"
// prediction-true bec bin a > bin A
// actual-true

//     "b" < "A"
// prediction-false bec bin b > bin A
// actual-false

//     true === false
// prediction- false bec true = 1 and false = 0
// actual-false

//     true != true
// prediction- false bec true is true
// actual-false

// Exercise 2 : Ask For Numbers
// Instructions
// Ask the user for a string of numbers separated by commas
// Console.log the sum of the numbers.
// Hint: use some string methods
// Examples
// "2,3"➞ 5

// let str = prompt("Please enter 2 numbers to be added to each other seperated by a comma (i.e. 1,2)");
// let arr = str.split(",");
// let num1 = +arr[0];
// let num2 = +arr[1];
// alert(num1 + num2);

// Exercise 3 : Find Nemo
// Instructions
// Hint: if statement (tomorrow’s lesson)

// Ask the user to give you a sentence containing the word “Nemo”. For example "I love the movie named Nemo"
// Find the word “Nemo”
// Console.log a string as follows: "I found Nemo at [the position of the word Nemo]".
// If you can’t find Nemo, console.log “I can’t find Nemo”.
// Some examples:

//     "I love the movie named Nemo" ➞ "I found Nemo at 5"
//     "Nemo is a cute fish" ➞ "I found Nemo at 0"
//     "My fish is called Nemo, I love it" ➞ "I found Nemo at 4"

// let sent = prompt("Please enter a sentence containing the word 'Nemo'");
// let arr = sent.split(" "); 
// if(arr.indexOf("Nemo") != -1){
//     alert("I found Nemo at " + arr.indexOf("Nemo"))
// } else if(arr.indexOf("nemo") != -1){
//     alert("I found Nemo at " + arr.indexOf("nemo"))
// } else (alert("I can\'t find Nemo"));



// Exercise 4 : Boom
// Instructions
// Hint: if statement (tomorrow’s lesson)

// Prompt the user for a number. Depending on the users number you will return a string of the word “Boom”. Follow the rules below:

// If the number given is less than 2 : return “boom”
// If the number given is bigger than 2 : the string should include n number of “o”s (n being the number given)
// If the number given is evenly divisible by 2, add a exclamation mark to the end.
// If the number given is evenly divisible by 5, return the string in ALL CAPS.
// If the number given is evenly divisible by both 2 and 5, return the string in ALL CAPS and add an exclamation mark to the end.
// Examples
// 4 ➞ "Boooom!"
// // There are 4 "o"s and 4 is divisible by 2 (exclamation mark included)
// 1 ➞ "boom"
// // 1 is lower than 2, so we return "boom"

let num = prompt("Please enter a number");
let str = '';
for (let i = 0; i < (num); i++){
    str=str+"o";
}
let STR = '';
for (let i = 0; i < (num); i++){
    STR=STR+"O";
}
if(isNaN(num) == true){
    alert("Refresh and enter only a number, no letters or symbols!")
}else if(num%2 == 0 && num%5 == 0 && num > 0){
    alert("B" + STR + "M!")
}else if(num%5 == 0 && num > 0){
    alert("B" + STR + "M")
} else if(num%2 == 0 && num > 0){
    alert("b" + str + 'm!')
} else if(num > 2){
    alert("b" + str + "m")
}else if(num < 2){
    alert("boom")
}



