"use strict";

// These are both in the global scope

var test = 1;
window.foo = 1;



// Functional or local scoped variables

function foo() {
  var moo = 1;
};

console.log(moo); // This will fail
