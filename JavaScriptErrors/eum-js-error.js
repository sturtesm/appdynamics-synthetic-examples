
  function rangeError()
  {
    var cars;

    console.log("Car Index Four = " + cars[4]);
  }

  function syntaxError()
  {
    throw new SyntaxError('This is a syntaxError', 'eum-error.html', 22);

  }

  function uriError() {
    console.log("URI Error");
    decodeURIComponent("%");
  }

  // Returns a random number between min (inclusive) and max (exclusive)
  function getRandomArbitraryInt(min, max) {
    var rnd = Math.random() * (max - min) + min;

    //return rnd.parseInt();

    return parseInt(rnd);
  }

  function randJavascriptError() {
    console.log("In DOMContentLoaded Event Listener");

     var index = getRandomArbitraryInt(1,4);

     console.log("index == " + index);

     try {
       if (index == 1) {
         missingFunction();
       }
       else if (index == 2) {
         rangeError();
       }
       else if (index == 3) {
         uriError();
       }
     }
     catch (e) {
       var errorT = new ADRUM.events.Error();

       console.log("Error [eum-js-error.js: " + e.lineNumber + " " + e.message);
       console.log("Reporting stack trace: \n" + e.stack);

       errorT.msg(e.message);
       errorT.line(e.lineNumber);
       errorT.stack(e.stack);
       ADRUM.report(errorT);
     }
   }
