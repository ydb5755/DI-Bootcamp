


const tasks = [];


let input = document.getElementById("input");
let btn = document.getElementById("btn");
let list = document.getElementById("theList");

btn.addEventListener("click", addTask);


console.log(list);
console.log(input);

function addTask(event){
    event.preventDefault();
    let text = document.createTextNode(input.value)
    let item = document.createElement("li");
    if(input.value.length > 0){
        item.appendChild(text);
        list.appendChild(item);
    }
};