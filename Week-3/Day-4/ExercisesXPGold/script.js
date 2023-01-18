// Exercise 1 : The World Translator
// Instructions
// Hint: Use Switch Case

// Ask the user which language they speak.

// Convert the user’s answer to lowercase, so that all the user’s inputs will be accepted in the if statement. For example “english” or “English” or “ENGlish” ect…”

// Create a few conditions :
// If the user speaks French : display “Bonjour”
// If the user speaks English : display “Hello”
// If the user speaks Hebrew : display “Shalom”
// If the user doesn’t speak any of these 3 languages: display ‘01110011 01101111 01110010 01110010 01111001’

// let lang = prompt("What language do you speak?");
// let ulang = lang.toLowerCase();
// switch (ulang) {
//     case "english":
//         alert("Hello!");
//         break;
//     case "hebrew":
//         alert("Shalom!");
//         break;
//     case "french":
//         alert("Bonjour!");
//         break;
//     default:
//         alert("01110011 01101111 01110010 01110010 01111001");
//         break;
// }

// Exercise 2 : The Grade Assigner
// Instructions
// Ask the user for their grade.

// If the grade is bigger than 90, console.log “A”

// If the grade is between 80 and 90 (included), console.log “B”
// If the grade is between 70(included) and 80 (included), console.log “C”
// If the grade is lower than 70, console.log “D”

// let grade = prompt("What grade did you receive?");
// switch (true) {
//     case isNaN(grade):
//         alert("Please retry and only enter a number grade");
//         break;
//     case grade > 90:
//         alert("A");
//         break;
//     case grade <=90 && grade > 80:
//         alert("B");
//         break;
//     case grade <=80 && grade >= 70:
//         alert("C");
//         break;
//     default:
//         alert("D");
//         break;
// }
    


// Exercise 3 : Verbing
// Instructions
// Prompt the user for a string. It must be a verb.
// If the length of the string is at least 3 and the string doesn’t end with “ing”, add ‘ing’ to the end of the string.
// If the length of the string is at least 3 and the string ends with “ing” add “ly” to it’s end.
// If the length of the string is less than 3, leave it unchanged.
// Example:

//   The string is : "swim" , your program should console.log : "swimming"
//   The string is : "swimming", your program should console.log : "swimmingly"
//   The string is : "go" your program should console.log : "go"
// let verb = prompt("Please enter a verb");
// switch (true){
//     case verb.length < 3:
//         alert(verb);
//         break;

//     case verb.length >= 3:
//     case confirmEnding(verb, "ing") == false:
//         alert(verb + "ing");
//         break;
        
//     case verb.length >= 3:
//     case confirmEnding(verb, "ing") == true:
//         alert(verb + "ly");
//         break;
        

// }