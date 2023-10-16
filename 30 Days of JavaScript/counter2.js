/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let initCount = init; // No member variable, so can't use 'this' keyword so in memory there's no way to dinguish if you said init =, so we create initCount to effectively act as a copy

    function increment() {
    
        return ++initCount; // So we modify the copy of the hidden state which is active forever as long as the object is
    
    }
    
    // All these functions (methods, because this is a class) have access to init, due to something called closure, making init a hidden state of counter and always accessible to the object not sure how this works in memory though.
 
    function decrement() {
    
        return --initCount;
    
    }

    function reset(){

        initCount = init; //Then when reset is called we just set it back to hidden state value.
        return initCount;

    }

    return{

        increment:increment,

        decrement: decrement,

        reset:reset 
    
    } // This is how you return an object. And the object this is returning is saying hey if you requested an increment then have that method compute it instead of reurning in each function like we would in Python

};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */