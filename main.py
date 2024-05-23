from bs4 import BeautifulSoup as soup
import wget
from requests import get


def main():
    url = "https://libgen.is/fiction/?q="
    title= input("Title:").replace(" ","+")
    url = url + title
    page_soup = soup(get(url).text,'html.parser')
    books_soup = soup.find_all(page_soup,"tr")
    books = []
    for book in books_soup:
        row  = []
        for col in book.find_all("td"):
            row.append(col)
        books.append(row)

    choice = 1
    download_book(books[choice])


def download_book(book):
    mirrors = [link['href'] for link in book[5].find_all("a")]
    down_link = str(soup(get(mirrors[0]).text,'html.parser').find("h2").find("a")['href'])
    wget.download(down_link,out="./downloads/"+book[0].text.strip()+"-"+book[2].text.strip().split("\n")[0])

if __name__=='__main__':
    main()