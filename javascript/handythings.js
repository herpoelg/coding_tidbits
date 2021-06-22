// adding properties to an object conditionally
let free = false;

const bookFly = {
    id: 1,
    title: 'In name of the fly',
    ...(!free && { price: 32 }),
};



free = true;

const bookBee = {
    id: 1,
    title: 'In name of the bee',
    ...(!free && { price: 32 }),
};

console.log(bookFly, bookBee);

//checking an objects property via 'in'
const bookDragon = { name: 'In name of the Dragonfly', pages: 1522 };
console.log('name' in bookDragon); // returns true
console.log('price' in bookDragon); // returns false