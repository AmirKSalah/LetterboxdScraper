from selenium import webdriver
from bs4 import BeautifulSoup

year = input("What decade do you want to search?")


browser = webdriver.Chrome()
url = 'https://letterboxd.com/films/popular/year/' + str(year)
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, features='html.parser')
results = soup.find(id="films-browser-list-container")
films = results.find_all("a")
print(films)
i = 1
for film in films:
    name = film.find("span", class_="frame-title")
    print(str(i) + "." + name.text)
    i += 1
    if i > 50:
        break
