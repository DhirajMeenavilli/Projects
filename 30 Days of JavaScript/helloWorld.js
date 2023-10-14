function HelloWorld() {

    return 'Hello World'

}

console.log(HelloWorld())


// From LC

/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    return function(...args) {

        return 'Hello World';
        
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */