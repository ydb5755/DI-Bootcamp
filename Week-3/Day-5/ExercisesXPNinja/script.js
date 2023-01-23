// Exercise 1 : Checking The BMI
// Instructions
// Hint:
// - You must use functions to complete this exercise, to do so take a look at tomorrow’s lesson.

// Create two objects, each object should hold a person’s details. Here are the details:
// FullName
// Mass
// Height
// let yisroel = {
//     Fullname: "Yisroel Baum",
//     Mass: 63,
//     Height: 1.70,
//     BMI: function (){
//         return this.Mass/(this.Height^2)
//     }
// }
// let emma = {
//     FullName: "Emma Baum",
//     Mass: 60,
//     Height:1.60,
//     BMI: function (){
//         return this.Mass/(this.Height^2)
//     }
// }
// if(yisroel.BMI > emma.BMI){
//     console.log("yisroel");
// }else{
//     console.log("emma");
// }
// Each object should also have a key which value is a function (ie. A method), that calculates the Body Mass Index (BMI) of each person

// Outside of the objects, create a JS function that compares the BMI of both objects.

// Display the name of the person who has the largest BMI.


// Exercise 2 : Grade Average
// Instructions
// Hint:
// - This Exercise is trickier then the others. You have to think about its structure before you start coding.
// - You must use functions to complete this exercise, to do so take a look at tomorrow’s lesson.

// In this exercise we will be creating a function which takes an array of grades as an argument and will console.log the average.

// Create a function called findAvg(gradesList) that takes an argument called gradesList.

// function findAvg(gradesList){
//     var sum = 0;
//     for(let i = 0; i < gradesList.length; i++){
//         sum += gradesList[i];
//     }
//     if(sum/gradesList.length > 65){
//         return "You passed!";
//     } else {
//         return "You failed and must repeat the course";
//     }
// }
// let grades = [12,54,23,89,54];
// console.log(findAvg(grades));
// Your function must calculate and console.log the average.

// If the average is above 65 let the user know they passed

// If the average is below 65 let the user know they failed and must repeat the course.
// Bonus Try and split parts 1,2 and 3,4 of this exercise to two separate functions.
// Hint One function must call the other.

// let grades = [12,54,23,89,54];
// function findAvg(gradesList){
//     var sum = 0;
//     for(let i = 0; i < gradesList.length; i++){
//         sum += gradesList[i];
//     }
//     return sum/gradesList.length;
// }
// function passing(average){
//     if(average > 65){
//         return "You passed!";
//     } else{
//         return "You failed and must repeat the course";
//     }
// }
// console.log(passing(findAvg(grades)));