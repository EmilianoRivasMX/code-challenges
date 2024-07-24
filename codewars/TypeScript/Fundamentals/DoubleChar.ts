/*
    Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

    Examples:
        * "String"      -> "SSttrriinngg"
        * "Hello World" -> "HHeelllloo  WWoorrlldd"
        * "1234!_ "     -> "11223344!!__  "
*/
export function doubleChar(str: string): string {
    const chars: string[] = str.split('')
    let doubleCharString = ''
    chars.forEach(char => {
        doubleCharString += char + char
    }); 
    return doubleCharString
}

export function doubleCharV2(str: string): string {
    let doubleCharString = '';
    for (let i = 0; i < str.length; i++) {
        doubleCharString += str[i] + str[i];
    }
    return doubleCharString;
}

export function doubleCharV3(str: string): string {
    return str.split('').map(char => char.repeat(2)).join('');
}

console.log(doubleCharV3("String"))
console.log(doubleCharV3("Hello World"))
console.log(doubleCharV3("1234!_ "))