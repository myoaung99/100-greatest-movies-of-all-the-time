from bs4 import BeautifulSoup
import requests
import requests_html

from requests_html import HTMLSession
 
WEB_PAGE = "https://www.empireonline.com/movies/features/best-movies-2/"
WEB_FILE = "./data/100_best_movies.html"

all_movies = []
 
# Using requests_html to render JavaScript
def get_web_page():
    # create an HTML Session object
    session = HTMLSession()
    # Use the object above to connect to needed webpage
    response = session.get(WEB_PAGE)
    # Run JavaScript code on webpage
    response.html.render()
 
    # Save web page to file
    with open(WEB_FILE, mode="w", encoding="utf-8") as fp:
        fp.write(response.html.html)
 
def read_web_file():
    try:
        open(WEB_FILE)
    except FileNotFoundError:
        get_web_page()
    finally:
        # Read the web page from file
        with open(WEB_FILE, mode="r", encoding="utf-8") as fp:
            content = fp.read()
        return BeautifulSoup(content, "html.parser")
 
# Read web file if it exists, load from internet if it doesn't exist
result = read_web_file()
all_h3_tag = result.find_all("h3")

# Adding the h3.name to the list
for tag in all_h3_tag:
    all_movies.append(tag.string)

# Renaming the last value in a movie list
temp = all_movies[-1]
all_movies[-1] = f"1)" + temp

# Reverse the movie list
all_movies.reverse()

# Create a movie.txt
with open("all movies", mode="w", encoding="utf-8") as fp:
    for movie in all_movies:
        fp.writelines(movie + "\n")