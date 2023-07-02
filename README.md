# Band Database

This is a terminal interface using Python to access a PostgreSQL database of band idelogies.
By searching for either a band or a band member, this tool will tell you their ideology and the ideology of related bands or band members respectively.

## Background

This tool was created as a project forming part of my Codecademy computer science course.

## Database

The database was created with PostgreSQL based on the ER diagram below:
![ER Diagram](https://github.com/AndreaDavies228/band_database/blob/main/ER%20Diagram.png)
It contains bands, their ideologies and a link to the band logo.
It also contains band members, which bands they've belonged to and when they joined or left.

## Sample Images

To be uploaded

## Instructions and Files

To run the tool, execute the Script.py file in Python 3.
The psychopg2 module is used to run database queries and tabulate is used to format the results.
The credentials to access the database are stored in a separate config file not uploaded to github. 

## Author

Andrea Davies - Design and Coding

## License 

This project is licensed under the CC0 1.0 Universal Creative Commons License - see the LICENSE.md file for details.

