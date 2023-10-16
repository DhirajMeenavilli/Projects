var map = function(arr, fn) { // arr and fn are hidden states thus I have no need to set them myself, or keep copying them in etc.
    
    // copyOfArr = arr;
    solution = [];
    for (let i = 0; i < arr.length; i++) {

        solution.push(fn(arr[i],i))


    }

    return solution

};