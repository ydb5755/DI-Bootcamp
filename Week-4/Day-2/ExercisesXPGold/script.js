// Exercise 1 : Is_Blank
// Instructions
// Write a program to check whether a string is blank or not.

// console.log(isBlank('')); --> true
// console.log(isBlank('abc')); --> false
function isBlank (str) {
    if(str === ''){
        return true;
    }else{
        return false;
    }
}
// Exercise 2 : Abbrev_name
// Instructions
// Write a JavaScript function to convert a string into an abbreviated form.
// console.log(abbrevName("Robin Singh")); --> "Robin S."

function abbrevName (str){
    str  = str.slice(0, str.indexOf(" ") + 2) + '.';
    return str;
}

// Exercise 3 : SwapCase
// Instructions
// Write a JavaScript function which takes a string as an argument and swaps the case of each character.
// For example :

// if you input 'The Quick Brown Fox' 
// the output should be 'tHE qUICK bROWN fOX'.
function swapCase(str){
    arr = str.split('');
    for(let i = 0; i < arr.length; i++){
        if(arr[i] == arr[i].toUpperCase()){
            arr[i] = arr[i].toLowerCase();
        }else {
            arr[i] = arr[i].toUpperCase();
        }
    }
    arr = arr.join('');
    return arr;
}
// console.log(swapCase('The Quick Brown Fox'));

// Exercise 4 : Omnipresent Value
// Instructions
// Create a function that determines whether an argument is omnipresent for a given array.
// A value is omnipresent if it exists in every subarray inside the main array.
// To illustrate:

// [[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]]
// // 3 exists in every element inside this array, so is omnipresent.
// Examples

function isOmnipresent(array, value){
    var includes = false;
    for(let i = 0; i <array.length ; i++){
        if(array[i].includes(value)){
            includes = true;
        }else {
            includes = false;
            break;
        }
        // for(let j = 0;j < array[i].length; j++){}
    }
    return includes;
}

console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1));
console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6));
// isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1) ➞ true
// isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6) ➞ false