# US Census MongoDB Scripts

**JS_scripts** - contains JS scripts for creating the database. Will populate the 'States' and 'Counties' collections but none of the others (working on this).
1. Creates:
    - 'States' collection with: state FIPS code and state name
    - 'Counties' collection with: full county FIPS code, county name, and state FIPS code
    - Empty 'OccupationByClassOfWorker' collection
    - Empty 'IndustryByOccupation' collection
    - Empty 'Education' collection
    - Empty 'Socioeconomic' collection

**py_scripts** - python scripts to pull from, and add to the DB. (Still a major work in progress)

### To Create the database

1.  Open 'create_database.js' file
    - Change 'DB_NAME' to whatever you want your database to be called
    - Replace the connection string with your connection string
    - Replace 'FILE_PATH' with the filepath to 'JS_scripts' directory in your machine
2.  Enter the MongoDB shell
3.  load 'create_database.js'

### Basic MongoDB Commands (MacOS)

To run MongoDB:
``` brew services start mongodb-community@6.0 ```

To stop MongoDB:
``` brew services stop mongodb-community@6.0 ```

To enter MongoDB Shell:
``` mongosh ```

To exit MongoDB Shell:
``` exit ```

To load a JS script: 
``` load(**script_filepath**) ```