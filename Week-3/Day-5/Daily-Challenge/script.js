// Instructions
// Write a JavaScript program that recreates the pattern below.
// Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out this tutorial of nested loops).
// Do this Daily Challenge by youself, without looking at the answers on the internet.
// *  
// * *  
// * * *  
// * * * *  
// * * * * *
// * * * * * *

let star = "*";
for (let i = 0; i < 6; i++){
    console.log(star);
    star += " *";
}

let star1 = "*";
for (let i = 0; i < 6; i++){
    for(let j = 0; j<6; j++){
        if(i ==j){
            console.log(star1);
            star1 += " *"
        }
    }
}