/**
 * 
 * Running this script will create the census database. This should only be run once.
 * 
 * To run this script on MacOS: 
 * 1. start mongodb service: 'brew services start mongodb-community@6.0'
 * 2. enter mongodb shell: 'mongosh'
 * 3. run 'load('**create_database.js filepath here**')
 * 4. enjoy
 * 
 */


// REPLACE 'testTDIdb' DB WITH YOUR PREFERRED DB NAME //
DB_NAME = 'TDIdb';

// REPLACE THIS STRING WITH YOUR CONNECTION STRING //
CONNECTION = 'mongodb://127.0.0.1:27017/' + DB_NAME;

// connecting to the database
DB = connect(CONNECTION);


// Creating and populating the 'States' collection
load('states_script.js');

// Creating and populating the 'Counties' collection
load('counties_script.js');

// Creating the categories
load('categories_script.js');



