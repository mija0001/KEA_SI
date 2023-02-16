import fs from 'fs';

var book;
fs.readFile("data/book.json", "utf8", (err, data) => {
    if (err) {
        console.error(err);
    } else {
        console.log(JSON.parse(data))
        //book = JSON.parse(data);
    }
});
console.log(book);