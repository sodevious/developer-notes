"use strict";

// Must be a string so that older browsers don't get caught up
// Top of function or file

// Why?
// Makes debugging easier
// Code will throw exceptions and fail loudly

// Without strict mode, variables are declared globally to the window
var test = 1;
// window.test == 1;

// Will prevent you from using protected words in future versions, ie  `let`

// Cannot delete variables, arguments or functions

// Can be used in functions specifically instead of globally
// Not recommended

function foo() {
  "use strict";
}


// Evaluate javascript expressions in a string
// Strict mode prevents `a` from being leaked out
eval("var a = 1")
