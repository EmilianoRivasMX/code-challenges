/*
    Create a function that a string and a single character, and returns an integer 
    of the count of occurrences the 2nd argument is found in the first one
*/
export function strCount(str: string, letter: string): number {
    let count: number = 0;
    const searchString: string = str.toLowerCase();

    for(let i = 0; i < str.length; i++) {
        if(searchString[i] === letter) {
            count ++;
        }
    }
    return count
}

export function strCountV2(str: string, letter: string): number {
    return str.toLowerCase().split("").filter(value => value == letter).length;
}

console.log(strCountV2("tHis StrIng", 'i'));