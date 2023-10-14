/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    
    return function() {

        return n++ //I'm not sure at all how this works, why is it incrementing on every call, and why is it = 10,11,12 not not 11,12,13 

    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */