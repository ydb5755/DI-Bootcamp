var bottlesRemaining = 0;
var countUp = 1;


while(isNaN(countDown)){
    var countDown = prompt('Please enter a number');
}

console.log(`${countDown} bottles of beer on the wall`);
console.log(`${countDown} bottles of beer`);
console.log(`Take ${countUp} down, pass it around`);
countDown -= countUp;
countUp++
console.log(`${countDown} bottles of beer on the wall`);
while(countDown > 0){
    console.log(`${countDown} bottles of beer on the wall`);
    console.log(`${countDown} bottles of beer`);
    console.log(`Take ${countUp} down, pass 'em around`);
    countDown -= countUp;
    countUp++
    if(countDown<0){
        console.log('No bottles of beer on the wall');
        break;
    }
    console.log(`${countDown} bottles of beer on the wall`);
}