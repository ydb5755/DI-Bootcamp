
var allBooks = [
    {
        title:'Harry Potter',
        author:'JK Rowling',
        image: 'http://embed.cdn.pais.scholastic.com/v1/products/identifiers/isbn/9780590353403/primary/renditions/600?useMissingImage=true',
        alreadyRead: true
    },
    {
        title:'Lord of the Rings',
        author:'JRR Tolkien',
        image: 'https://www.dymocks.com.au/Pages/ImageHandler.ashx?q=9780261103252&w=&h=570',
        alreadyRead: true
    }
];
let row1 = document.querySelector('tr');
let row2 = row1.nextSibling.parentNode;
console.log(row2);
let rows = [row1, row2]

let img1 = document.createElement('img');
img1.style.width = '100px';
img1.src = allBooks[0].image;

let img2 = document.createElement('img');
img2.style.width = '100px';
img2.src = allBooks[1].image;

let text1 = document.createTextNode(`${allBooks[0].title} by ${allBooks[0].author}`);
let text2 = document.createTextNode(`${allBooks[1].title} by ${allBooks[1].author}`);

for(let obj in allBooks){
    if(allBooks[obj].alreadyRead == true){
        rows[obj].style.color = 'red';
    }
}

row1.appendChild(text1);
row1.appendChild(img1);
row2.appendChild(text2);
row2.appendChild(img2);