from selenium import webdriver
from bs4 import BeautifulSoup
print("~~Welcome to the Letterboxd Scraper! This tool will give you the 50 most popular movies during a certain time, "
      "as determined by Letterboxd.~~")
url = 'https://letterboxd.com/films/popular/'
response = input("Would you like to search by decade, year, or all-time?\n")
if response.lower() == 'decade':
    response = input("What decade would you like to search? (ex 1990s, 2010s, 2020s)\n")
    url = 'https://letterboxd.com/films/popular/decade/' + str(response)
elif response.lower() == 'year':
    response = input("What year would you like to search? (ex 1931, 1994, 2021)\n")
    url = 'https://letterboxd.com/films/popular/year/' + str(response)
elif response.lower() == 'all-time' or response.lower() == 'all time':
    url = 'https://letterboxd.com/films/popular/'
else:
    print("Input not recognized. Sorting by all-time")
browser = webdriver.Chrome()
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, features='html.parser')
results = soup.find(id="films-browser-list-container")
films = results.find_all("a")
i = 1
for film in films:
    name = film.find("span", class_="frame-title")
    print(str(i) + "." + name.text)
    i += 1
    if i > 50:
        break
