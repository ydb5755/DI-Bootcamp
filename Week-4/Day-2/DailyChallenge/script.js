// Instructions
// Prompt the user for several words (separated by commas).
let words = prompt("Please enter several words separated by commas");
// Put the words into an array.
let arr = words.split(",");
// Console.log the words one per line, in a rectangular frame as seen below.
// Check out the Hints and Requirements below.
function longest(array){
    let longWord = "";
    for(let i = 0; i < array.length; i++){
        if(longWord.length < array[i].length){
            longWord = array[i];
        }
    }
    return longWord.length;
}
let star = "*";
console.log(`**${star.repeat(longest(arr))}**`);


// Hint
// The number of stars that wraps the sentence, must depend on the length of the longest word.


// Requirements
// To do this challenge you only need Javascript(No HTML and no CSS)