// 🌟 Exercise 1: Your Favorite Food
// Instructions
// Store your favorite food into a variable.

// Store your favorite meal of the day into a variable (ie. breakfast, lunch or dinner)

// Console.log I eat <favorite food> at every <favorite meal>

// let favFood = "Lasagna";
// let favMeal = "Lunch";
// console.log("I eat " + favFood + " at every " + favMeal);

// 🌟 Exercise 2 : Series
// Instructions
// Part I
// Using this array : const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];

// Create a variable named myWatchedSeriesLength that is equal to the number of series in the myWatchedSeries array.

// Create a variable named myWatchedSeriesSentence, that is equal to a sentence describing the series you watched
// For example : black mirror, money heist, and the big bang theory

// Console.log a sentence using both of the variables created above
// For example : I watched 3 series : black mirror, money heist, and the big bang theory

// const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
// let myWatchedSeriesLength = myWatchedSeries.length;
// let myWatchedSeriesSentence = myWatchedSeries.toString();
// myWatchedSeriesSentence = myWatchedSeriesSentence.replaceAll(',',', ');
// myWatchedSeriesSentence = myWatchedSeriesSentence.slice(0, myWatchedSeriesSentence.lastIndexOf(',')) + ", and " + myWatchedSeriesSentence.slice(myWatchedSeriesSentence.indexOf('the'));
// let finalSentence = "I watched " + myWatchedSeriesLength + " series : " + myWatchedSeriesSentence;
// console.log(finalSentence);

// Part II
// Change the series “the big bang theory” to “friends”. Hint : You will need to use the index of “the big bang theory” series.
// Add, at the end of the array, the name of another series you watched.
// Add, at the beginning of the array, the name of your favorite series.
// Delete the series “black mirror”.
// Console.log the third letter of the series “money heist”.
// Finally, console.log the myWatchedSeries array, to see all the modifications you’ve made.

// myWatchedSeries[2] = "friends";
// myWatchedSeries.push("prison break");
// myWatchedSeries.unshift("seinfeld");
// myWatchedSeries.splice(1,1);
// console.log(myWatchedSeries[1][2]);
// console.log(myWatchedSeries);


// 🌟 Exercise 3 : The Temperature Converter
// Instructions
// Store a celsius temperature into a variable.

// Convert it to fahrenheit and console.log <temperature>°C is <temperature>°F.
// Hint : Should you create another variable to hold the temperature in fahrenheit? (ie. point 2)
// Hint: To convert a temperature from celsius to fahrenheit : Divide it by 5, then multiply it by 9, then add 32

// let C = 100;
// let F = (C/5*9)+32;
// console.log(C + "C is " + F + "F");


// 🌟 Exercise 4 : Guess The Answers #1
// Instructions
// For each expression, predict what you think the output will be in a comment (//) without first running the command.
// Of course, explain each prediction.
// Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.



// For example

// console.log(2+3)
// // Prediction: It will output 5, because 2 and 3 are numbers
// // Actual: 5


// Using the code below:

//     let c;
//     let a = 34;
//     let b = 21;

//     console.log(a+b) //first expression
// //     // Prediction:55 a and b are numbers
// //     // Actual:55

//     a = 2;

//     console.log(a+b) //second expression
//     // Prediction:23 because a was changed and b stayed the same
//     // Actual:23



// // What will be the outcome of a + b in the first expression ? 
// 55
// // What will be the outcome of a + b in the second expression ? 
// 23
// // What is the value of c? 
// undefined

// Analyse the code below, what will be the outcome? 
// console.log(3 + 4 + '5');

// Exercise 5 : Guess The Answers #2
// Instructions
// For each expression, predict what you think the output will be in a comment (//) without first running the command.
// Of course, explain each prediction.
// Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.



// For example

// typeof("potato")
// // Prediction: Vegetable
// // Actual: String


// What is the output of each of the expressions below?


// typeof(15)
// // Prediction: number, its not in quotes to make it string
// // Actual: number

// typeof(5.5)
// // Prediction: number
// // Actual: number

// typeof(NaN)
// // Prediction: number
// // Actual:number

// typeof("hello")
// // Prediction: String because its wrapped in quotes
// // Actual:string

// typeof(true)
// // Prediction: Boolean - boolean values are true or false
// // Actual:boolean

// typeof(1 != 2)
// // Prediction: boolean - its either true or false
// // Actual: boolean

// "hamburger" + "s"
// // Prediction:hamburgers - combination of two strings
// // Actual:hamburgers

// "hamburgers" - "s"
// // Prediction:error
// // Actual:NaN

// "1" + "3"
// // Prediction:13 - this is adding two strings which puts them next to each other, not making a calculation
// // Actual:13

// "1" - "3"
// // Prediction:NaN - cant subtract from strings, subraction is limited to number calculations
// // Actual:-2

// "johnny" + 5
// // Prediction:NaN - its trying to connect a string and a number which results in error
// // Actual:johnny5

// "johnny" - 5
// // Prediction:NaN - its trying to subtract a string and a number which results in error
// // Actual:NaN

// 99 * "hello"
// // Prediction:NaN - trying to calculate a number and string = error
// // Actual:NaN

// 1 != 1
// // Prediction: false - this is a boolean request which returns false
// // Actual:false

// 1 == "1"
// // Prediction: true- using == doesnt check for type, and the values here do equal each other
// // Actual:true

// 1 === "1"
// // Prediction:false - using === checks for pure match including value and type and this is comparing a string and a number which returns false
// // Actual:false

// Exercise 6 : Guess The Answers #3
// Instructions
// For each expression, predict what you think the output will be in a comment (//) without first running the command.
// Of course, explain each prediction.
// Then run the expression in the console. Note the actual output in a comment and compare it with your prediction.



// What is the output of each of the expressions below?

// 5 + "34"
// // Prediction:534 - adding a number in front of a string
// // Actual:534

// 5 - "4"
// // Prediction:1 - doing this will calculate the value of 4 subtracted from 5
// // Actual:1

// 10 % 5
// // Prediction:0 - 10 over 5 = 2 with no remainder so this is 0
// // Actual:0

// 5 % 10
// // Prediction:5 - 5 over 10 is not a whole number so it returns 0 with a remainder of 5
// // Actual:5

// "Java" + "Script"
// // Prediction:JavaScript - adding two strings puts one in front of the other
// // Actual:JavaScript

// " " + " "
// // Prediction:"  " - adding two spaces together 
// // Actual:"  "

// " " + 0
// // Prediction: 0 - space in front of the zero
// // Actual: 0

// true + true
// // Prediction: true - boolean calculation
// // Actual: 2 

// true + false
// // Prediction:false
// // Actual: 1 

// false + true
// // Prediction: 1 
// // Actual:1

console.log("Bob" - "bill");
// false - true
// // Prediction: -1
// // Actual: -1

// !true
// // Prediction: false - not true
// // Actual: false

// 3 - 4
// // Prediction: -1
// // Actual:

// "Bob" - "bill"
// // Prediction:NaN
// // Actual:NaN
