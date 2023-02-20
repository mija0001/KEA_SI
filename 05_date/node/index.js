console.log(new Date());

// get date as a unix timestamp
console.log(new Date().getDate());


/* Region specific */
console.log("====== Region specific ======");
const date = new Date();
console.log(new Intl.DateTimeFormat('en-US').format(date));
console.log(new Intl.DateTimeFormat('en-DK').format(date));