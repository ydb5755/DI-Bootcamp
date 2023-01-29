// Exercise 1: Random Number
// Instructions
// Get a random number between 1 and 100.
// Console.log all even numbers from 0 to the random number.

// const random  = Math.round((Math.random()*99)+1);
// for(let i = 0; i < random; i++){
//     if(i%2 == 0){
//         console.log(i);
//     }
// }


// Exercise 2: Capitalized Letters
// Instructions
// Create a function that takes a string as an argument.
// Have the function return:
// The string but all letters in even indexes should be capitalized.
// The string but all letters in odd indexes should be capitalized.
// Note:

// Index 0 will be considered even.
// The argument of the function should be a lowercase string with no spaces.
// For example,

// capitalize("abcdef") will return ['AbCdEf', 'aBcDeF']


// function capitalize(string){
//     let result =[];
//     let even = string.split('');
//     let odd = string.split('');
//     for(let i = 0;i < even.length;i++){
//         if(i%2 == 0){
//             even[i] = even[i].toUpperCase();
//         }
//     }
//     for(let i = 0;i < odd.length;i++){
//         if(i%2 == 1){
//             odd[i] = odd[i].toUpperCase();
//         }
//     }
//     even = even.join('');
//     odd = odd.join('');
//     result.push(even);
//     result.push(odd);
//     return result;
// }
// console.log(capitalize("abcdef"));

// Exercise 3 : Is Palindrome?
// Instructions
// Write a JavaScript function that checks whether a string is a palindrome or not.
// Note A palindrome is a word, phrase or sequence that is spelled the same both backwards and forward, e.g., madam, bob or kayak.
// palindrome

// function isPalindrome(string){
//     string = string.split(' ').join('')
//     string = string.toLowerCase();
//     let len = string.length;
//     let mid = (len + 1)/2 - 1;
//     let mid1 = mid + .5;
//     let mid2 = mid - .5;
//     let midToEndLenOdd = len - mid;
//     let midToEndLenEven = len - (len/2);
//     let result = false;
//     if(len%2 == 0){
//         for(let i = 0; i < midToEndLenEven; i++){
//             if(string[mid1+i] == string[mid2-i]){
//                 console.log(string[mid1+i]);
//                 result = true;
//             }else{
//                 result = false;
//                 break;
//             }
//         }
//     }else{
//         for(let i = 1; i < midToEndLenOdd + 1; i++){
//             if(string[mid+i] == string[mid-i]){
//                 result = true;
//             }else{
//                 result = false;
//                 break;
//             }
//         }
//     }
//     return result;
// }
// console.log(isPalindrome('111'));
// console.log(isPalindrome('horse'));
// console.log(isPalindrome('bob'));


// Exercise 4 : Biggest Number
// Instructions
// Create a function called biggestNumberInArray(arrayNumber) that takes an array as a parameter and returns the biggest number.
// Note : This function should work with any array;
// Example:

// function bigggestNumberInArray(array){
//     let greatest = 0;
//     for (let i = 0; i < array.length; i++){
//         if(isNaN(array[i])){
//             continue;
//         }else if(array[i] > greatest){
//             greatest = array[i];
//         }
//     }
//     return greatest;
// }

// const array = [-1,0,3,100, 99, 2, 99] ;// should return 100 
// const array2 = ['a', 3, 4, 2]; // should return 4 
// const array3 = []; // should return 0

// Exercise 5: Unique Elements
// Instructions
// Write a JS function that takes an array and returns a new array with only unique elements.

// Example list=[1,2,3,3,3,3,4,5] newList = [1,2,3,4,5]
// Example list=[1,2,3,3,3,3,4,5] newList = [1,2,3,4,5]
// function unique(array){
//     let newArray = [];
//     for(let i = 0; i < array.length;i++){
//         if(newArray.includes(array[i])){
//             continue;
//         }else{
//             newArray.push(array[i]);
//         }
//     }
//     return newArray;
// }
// let list = [1,2,3,3,3,3,4,4,4,4,5,5,5,5,5,5,5,2];
// console.log(unique(list));