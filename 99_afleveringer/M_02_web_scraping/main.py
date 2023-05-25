import requests # Module for making HTTP requests
from bs4 import BeautifulSoup # Module for parsing HTML
import mysql.connector
import credentials # Local credentials file to prevent publishing credentials to GitHub


### Scraping the Star Wars saga ###
html = requests.get("https://starwars.fandom.com/wiki/Star_Wars_saga").text # Get the HTML from the URL
parsed_html = BeautifulSoup(html, "lxml") # Parse the HTML with BeautifulSoup, making it searchable

tags = parsed_html.find("div", {"class": "mw-parser-output"}) # Find the div tag with the class "mw-parser-output", containing the content of the page

films = {} # Output dictionary for the films

current_trilogy = None # Variable for keeping track of the current trilogy

for tag in tags:
    if tag.name == "h2" and tag.text.startswith("Films"): # Find the Films section
        for subtag in tag.find_next("ul"): # Find the first ul tag after the Films section, containing the trilogies
            if subtag.name == "li": # Find each li tag in the ul tag, containing the individual trilogies
                current_trilogy = subtag.next_element.text.replace("\n", "") # Get the name of the trilogy from the li tag, remove superfluous newline
                films[current_trilogy] = [] # Create a list for the films in the trilogy
                for film in subtag.find_next("ul"): # Find the first ul tag after the trilogy li tag, containing the films
                    if film.name == "li": # Find each li tag in the ul tag, containing the individual films
                        films[current_trilogy].append(film.text) # Add the film to the list of films in the trilogy
            

### Saving the Star Wars saga to the database ###
# Connect to the database
def connect_to_database():
        # Connect to the database
        db = mysql.connector.connect(
            host=credentials.host,
            user=credentials.command_user,
            password=credentials.command_password,
            database=credentials.database
        )
        # Create a cursor
        cursor = db.cursor()
        return db, cursor


# Add a film to the database, if it does not already exist
def add_film(film, trilogy):
        db, cursor = connect_to_database()
        sql = "INSERT INTO films (film, trilogy) " \
                "SELECT %s, %s " \
                "WHERE NOT EXISTS (SELECT 1 FROM films WHERE film = %s)"
        val = (film, trilogy, film)
        cursor.execute(sql, val)
        db.commit()
        db.close()


# Add the films from the scrape to the database
for trilogy in films:
    for film in films[trilogy]:
        add_film(film, trilogy)