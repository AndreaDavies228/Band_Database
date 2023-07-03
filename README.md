# Band Database

This is a terminal interface using Python to access a PostgreSQL database of band idelogies.
By searching for either a band or a band member, this tool will tell you their ideology and the ideology of related bands or band members respectively.

## Background

This tool was created as a project forming part of my Codecademy computer science course.

## Sample Images

To be uploaded

## Instructions and Files

To run the tool, execute the Script.py file in Python 3.
The credentials to access the database are stored in a separate config file not uploaded to github. Please use this tool with your own database, or make a request for access.

setup.py can be used with py2exe to create a windows executable file, allowing those without python or coding knowledge to use the tool and access the database.

The psychopg2 module is used to run database queries and tabulate is used to format the results.
Functions that access the database are contained in the queries.py file, while other functions are in functions.py.

## Current Limitations

The following limitations are planned to be addressed in a future update:

* It's not possible to enter multiple bands or band members with the same name
* The search function relies on perfect matches (case insensitive)

## Author

Andrea Davies - Design and Coding

## License 

This project is licensed under the CC0 1.0 Universal Creative Commons License - see the LICENSE.md file for details.

## Database

The database was created with PostgreSQL based on the ER diagram below:
![ER Diagram](https://github.com/AndreaDavies228/band_database/blob/main/ER%20Diagram.png)

It contains bands, their ideologies and a link to the band logo.
It also contains band members, which bands they've belonged to and when they joined or left.

The database can be recreated with the following queries:

CREATE TABLE bands(
id SERIAL PRIMARY KEY,
name varchar UNIQUE,
ideology varchar
);

CREATE TABLE members(
id SERIAL PRIMARY KEY,
name varchar UNIQUE,
ideology varchar
);

CREATE TABLE bands_members(
id SERIAL unique,
band_id integer REFERENCES bands(id) on delete cascade,
member_id integer REFERENCES members(id) on delete cascade,
primary key (band_id, member_id)
);

CREATE TABLE logos (
id SERIAL PRIMARY KEY,
band_id integer REFERENCES bands(id) on delete cascade,
logo varchar 
);

create table timeframes(
id SERIAL primary key,
bands_members_id integer REFERENCES bands_members (id) on delete cascade,
joined_year integer,
left_year integer
);
