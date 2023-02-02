let planets = [
    { name: "Mercury", moons: 0}, 
    { name: "Venus", moons: 0}, 
    { name: "Earth", moons: 1}, 
    { name: "Mars", moons: 0}, 
    { name: "Jupiter", moons: 2}, 
    { name: "Saturn", moons: 3}, 
    { name: "Uranus", moons: 4}, 
    { name: "Neptune", moons: 0}
];


for(const planet of planets){
    const planetDiv = document.createElement("div");
    planetDiv.classList.add("planet");
    planetDiv.classList.add(planet.name);
    // console.log(planet);
    document.querySelector('section').appendChild(planetDiv);

    for( let i = 0; i < planet.moons; i++){
        const moonDiv = document.createElement("div");
        moonDiv.classList.add("moon");
        moonDiv.style.left = i * 10 + "px";
        planetDiv.appendChild(moonDiv);
    }
}
// console.log(sect);



// let sun = document.createElement('div');
// sun.classList.add('planet', 'sun');
// sun.style.backgroundColor = 'yellow';
// document.querySelector('section').append(sun);

// let mercury = document.createElement('div');
// mercury.classList.add('planet', 'mercury');
// mercury.style.backgroundColor = 'red';
// document.querySelector('section').append(mercury);
// console.log(document.querySelector('section'));