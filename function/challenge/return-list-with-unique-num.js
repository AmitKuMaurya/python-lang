let nums = [9,9,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1,1];

function printUnique (numbers) {
    
    // console.log(numbers.length);
    let array = [];
    for(let i=0;i<numbers.length;i++){
        if(numbers.includes(i)){
            array.push(i);
        }
    }
    return array;

}

console.log(printUnique(nums));


function fun(name = "amit",age){
    return (`my name is ${name}. and I'm ${age} years old.`)
}
console.log(fun("amit",22))