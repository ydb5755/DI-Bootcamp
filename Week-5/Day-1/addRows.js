



var num = 3;
function insertRow(){
    const savedRow = document.getElementById("sampleTable").firstElementChild.lastElementChild;
    const newRow = document.createElement('tr');
    const cell1 = document.createElement('td');
    const cell2 = document.createElement('td');
    cell1.innerText = `Row${num} cell1`;
    cell2.innerText = `Row${num} cell2`;
    num++
    newRow.appendChild(cell1);
    newRow.appendChild(cell2);
    savedRow.parentNode.appendChild(newRow);
}