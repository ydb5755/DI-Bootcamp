


function playTheGame(){
    var answer = confirm("Would you like to play?");
    if(answer == false){
        alert("No problem, Goodbye");
    }else{
        var num = prompt("Please enter a number between 0 and 10 (inclusive)");
        if(isNaN(num)){
            alert("Sorry Not a number, Goodbye");
        }else if(num >= 10 || num <= 0){
            alert("Sorry it\'s not a good number, Goodbye");
        }else{
            var computerNumber = Math.round(Math.random() * 10);
            var final = compareNumbers(num, computerNumber);
        }
    }
    return final;
}

function compareNumbers(userNumber,computerNumber){
    for(let i = 0; i < 3; i++){
        if(userNumber == computerNumber){
            alert("WINNER!");
            break;
        }else if(userNumber > computerNumber){
            alert("Your number is greater than the computer\'s, guess again");
            if(i == 2){
                alert("out of chances");
                break;
            }else{
                userNumber = prompt("Please enter a number between 0 and 10 (inclusive)");
                if(userNumber == null){
                    alert("No problem, Goodbye");
                    break;
                }else if(isNaN(userNumber) == true){
                    alert("Sorry Not a number, Goodbye");
                    break;
                }else if(userNumber >= 10 || userNumber <= 0){
                    alert("Sorry it\'s not a good number, Goodbye");
                    break;
                }
            }
        }else if(userNumber < computerNumber){
            alert("Your number is smaller than the computer\'s, guess again");
            if(i == 2){
                alert("out of chances");
                break;
            }else{
                userNumber = prompt("Please enter a number between 0 and 10 (inclusive)");
                if(userNumber == null){
                    alert("No problem, Goodbye");
                    break;
                }else if(isNaN(userNumber) == true){
                    alert("Sorry Not a number, Goodbye");
                    break;
                }else if(userNumber >= 10 || userNumber <= 0){
                    alert("Sorry it\'s not a good number, Goodbye");
                    break;
                }
            }
        }
        
    }
}
