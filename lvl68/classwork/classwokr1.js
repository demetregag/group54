const logicalFunc = function(a, b) {
  console.log(a && b);
  console.log(a || b);
};

logicalFunc(false, true);
logicalFunc(true, true);
logicalFunc(false, false);
