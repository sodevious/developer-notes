"use strict";

// These are both in the global scope

var test = 1;
window.foo = 1;



// Functional or local scoped variables

function foo() {
  var moo = 1;
};

console.log(moo); // This will fail


// Scope chain is defined lexically
// in the order that it's written in the page instead of how functions are called
// Functions look in their scope then outer scope
