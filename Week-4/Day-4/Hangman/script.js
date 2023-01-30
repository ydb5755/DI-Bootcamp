var secretWord = '';
while(secretWord.length < 8){
    secretWord = prompt("Please enter a word with a minimum of 8 letters");
    if(secretWord == null){
        console.log('Ok, Goodbye');
        break;
    }
}
secretWord = secretWord.toLowerCase();

var secretWordArray = secretWord.split('');
console.log(secretWordArray);
var secretStar = "*".repeat(secretWord.length);
var secretStarArray = secretStar.split('');
console.log(secretStarArray);
console.log(secretStar);

var wrongGuessCount = 0;
var guessList = [];
while(wrongGuessCount < 11){
    console.log(guessList);
    var guess = prompt("Guess a letter!");
    var letters = /^[A-Za-z]+$/;
    if(guess == null){
        console.log('Ok, Goodbye');
        break;
    }
    if(guess.length > 1 || guess == ''){
        console.log('Not a valid entry, please enter one letter at a time');
        continue;
    }
    if(isNaN(guess) == false || letters.test(guess) == false){
        console.log('Not a valid entry, please enter letters only');
        continue;
    }
    guess = guess.toLowerCase();
    if(guessList.includes(guess)){
        console.log("You already chose this letter, please choose another");
        console.log(`You have ${guessesRemaining} guesses remaining`);
    } else if(secretWordArray.includes(guess)){
        console.log('You guessed correct!');
        for(let i = 0;i < secretWordArray.length;i++){
            if(secretWordArray[i] == guess){
                secretStarArray[i] = guess;
            }
        }
        console.log(secretStarArray.join(''));
        guessList.push(guess);
    }else {
        console.log("Sorry, that letter is not in the secret word");
        guessList.push(guess);
        wrongGuessCount += 1;
        var guessesRemaining = 10 - wrongGuessCount;
        console.log(`You have ${guessesRemaining} guesses remaining`);
    }
    if(secretStarArray.join('') == secretWord){
        console.log(`You won! The secret word is ${secretWord}`);
        break;
    }
    if(wrongGuessCount == 10){
        console.log('YOU LOSE!');
        break;
    }
}

