/*
    Write a 'welcome' function that takes a parameter 'language', with a type String, 
    and returns a greeting - if you have it in your database. 
    
    It should default to English if the language is not in the database, 
    or in the event of an invalid input.

    Possible invalid inputs include:
        IP_ADDRESS_INVALID - not a valid ipv4 or ipv6 ip address
        IP_ADDRESS_NOT_FOUND - ip address not in the database
        IP_ADDRESS_REQUIRED - no ip address was supplied
*/

export function greet(language: string): string {
    const database = {
        "english": "Welcome",
        "czech": "Vitejte",
        "danish": "Velkomst",
        "dutch": "Welkom",
        "estonian": "Tere tulemast",
        "finnish": "Tervetuloa",
        "flemish": "Welgekomen",
        "french": "Bienvenue",
        "german": "Willkommen",
        "irish": "Failte",
        "italian": "Benvenuto",
        "latvian": "Gaidits",
        "lithuanian": "Laukiamas",
        "polish": "Witamy",
        "spanish": "Bienvenido",
        "swedish": "Valkommen",
        "welsh": "Croeso"
    };

    return language in database ? database[language] : 'Welcome';
}

export function greetV2(language: string): string {
    const database: {[key: string]: string} = {
        "english": "Welcome",
        "czech": "Vitejte",
        "danish": "Velkomst",
        "dutch": "Welkom",
        "estonian": "Tere tulemast",
        "finnish": "Tervetuloa",
        "flemish": "Welgekomen",
        "french": "Bienvenue",
        "german": "Willkommen",
        "irish": "Failte",
        "italian": "Benvenuto",
        "latvian": "Gaidits",
        "lithuanian": "Laukiamas",
        "polish": "Witamy",
        "spanish": "Bienvenido",
        "swedish": "Valkommen",
        "welsh": "Croeso"
    };

    if (language in database) {
        return database[language]
    };
    
    return 'Welcome';
}

console.log(greet('dutch'))
console.log(greet('IP_ADDRESS_INVALID'))