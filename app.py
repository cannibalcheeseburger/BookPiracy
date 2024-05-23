# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
from bs4 import BeautifulSoup as soup
import wget
from requests import get


# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

@app.route('/<title>')
def get_books(title):
    url = "https://libgen.is/fiction/?q="
    url = url + title
    page_soup = soup(get(url).text,'html.parser')
    books_soup = soup.find_all(page_soup,"tr")
    books = []
    for book in books_soup:
        row  = []
        for col in book.find_all("td"):
            row.append(col)
        books.append(row)
    return books

@app.route('/<title>/<choice>')
def get_book(title,choice):
    url = "https://libgen.is/fiction/?q="
    url = url + title
    page_soup = soup(get(url).text,'html.parser')
    books_soup = soup.find_all(page_soup,"tr")
    books = []
    for book in books_soup:
        row  = []
        for col in book.find_all("td"):
            row.append(col)
        books.append(row)        
    download_book(books[choice])
    return 'Downloaded:'+ books[choice].text

def download_book(book):
    mirrors = [link['href'] for link in book[5].find_all("a")]
    down_link = str(soup(get(mirrors[0]).text,'html.parser').find("h2").find("a")['href'])
    wget.download(down_link,out="./downloads/"+book[0].text.strip()+"-"+book[2].text.strip().split("\n")[0])


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
