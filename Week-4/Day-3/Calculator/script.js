var displayDiv = '';


function equal(eq){

}
function operator(op){
    if(isNaN(displayDiv.slice(-1))){
        return;
    }else{
        displayDiv += op;
        document.getElementById("display").textContent = displayDiv;
        return;
    }
}
function number(num){
    displayDiv += num;
    document.getElementById("display").textContent = displayDiv;
    return;
}


function reset(){
    displayDiv = '';
    document.getElementById("display").textContent = displayDiv;
    return;
}

document.getElementById("display").textContent = displayDiv;