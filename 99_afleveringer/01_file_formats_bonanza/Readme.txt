--- Task ---
Create new files in at least these formats: text, xml, yaml, json, csv.
You decide the content.

Create scripts that can read and parse the files in 2 programming languages of your choice.

--- Data files ---
Data file path: 99_afleveringer\01_file_formats_bonanza\files

--- Java solution ---
### Parser class has methods with a filepath parameter for a txt, csv, xml, json or yaml file, 
    containing the data fields for a single book, the methods return a BookData object containing the data from the file.
### Main class has a main method that runs every parser method in Parser, and prints a representation of the resulting BookData object.
### BookData class is data class, which has data fields representing a book, and a toString method for testing.

Parser class path: 99_afleveringer\01_file_formats_bonanza\java\src\main\java\Parser.java
Main class path: 99_afleveringer\01_file_formats_bonanza\java\src\main\java\Main.java
BookData class path: 99_afleveringer\01_file_formats_bonanza\java\src\main\java\BookData.java

--- Python solution ---
### parser_classes module has a BookParser class with methods with a filepath parameter for a txt, csv, xml, json or yaml file,
    containing the data fields for a single book, the methods return a BookData object containing the data from the file.
### main.py has code to that runs every parser method in BookParser, and prints a representation of the resulting BookData object.
### data_classes module has a BookData class, which has the data fields representing a book, and a to_string method for testing.

parser_classes module path: 99_afleveringer\01_file_formats_bonanza\python\data_classes.py
main.py path: 99_afleveringer\01_file_formats_bonanza\python\main.py
data_classes module path: 99_afleveringer\01_file_formats_bonanza\python\parser_classes.py