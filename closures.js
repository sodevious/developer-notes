// Function closures

function sayHello(name) {
  var greeting = 'Hello' + name;

  return function() {
    console.log(text);
  }
};

sayHello("Nicole"); // "Hello Nicole"

sayHello("Nicole")(); // Returns the function instead

var sayNicole = sayHello("Nicole");
sayNicole(); = // "Hello Nicole"

// when a function returns a function, it keeps a reference to any variables that it needs to execute
