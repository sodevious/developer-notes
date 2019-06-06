console.log(this); // Returns window object

this.foo = 1;

console.log(this.foo); // 1
console.log(window.foo); // 1
console.log(foo); // 1


function checkThis () {
  console.log(this); 
}
  
checkThis(); // points to global window object


var nicole = {
  // a method
  
  checkThisAgain: function() {
    console.log(this); 
  }
}

console.log(nicole); // points to checkThisAgain onject
