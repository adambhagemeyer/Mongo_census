
//Create the states collection
DB.createCollection('Counties');

// split the counties file into an array
const {readFileSync, promises: fsPromises, linkSync} = require('fs');

// turn the text file into an array. Each line is a string
var lines = readFile(FILE_PATH.concat('counties.txt'));

// Remove the first and last line from the text file
lines.pop();
lines.shift();

try {
    lines.forEach((item) => {
        // further split this index into another array
        let text = item.trim().split(/\s+/);

        // Assign the fips code
        let fips_code = text[1]

        // Loop for ensuring that the entire county name is assigned
        let y = 4;
        let county_name_string = text[3]
        while (!containsNumbers(text[y])) {
            county_name_string += ' ';
            county_name_string += text[y];
            y++;
        }

        // Assign the state code as the first 2 numbers in the fips code
        state_code_string = text[1].slice(0, 2);

        // Add the counties to the database
        DB.Counties.insertOne( {
            fips: fips_code,
            county_name: county_name_string,
            state_code: state_code_string  
        } );
        
    });

} catch (e) {
    console.log("Error " + e);
}


// reads in the counties.txt file and returns an array containing each new line
function readFile(filename) {
    const contents = readFileSync(filename, 'utf-8');

    const arr = contents.split(/\r?\n/);

    return arr;
}

// checks if a string contains any numbers
function containsNumbers(stri) {
    let matchPattern = stri.match(/\d+/g);
    if (matchPattern !== null) {
        return true;
    }
    
    return false;
}