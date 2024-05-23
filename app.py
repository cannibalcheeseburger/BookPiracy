# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,render_template,request,url_for,redirect
from bs4 import BeautifulSoup as soup
import wget
from requests import get

app = Flask(__name__)


@app.route('/', methods =["GET", "POST"])
def home():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       mirror = request.form.get("mirror")
       return redirect(url_for('download_link')+"?mirror="+mirror)
    return render_template("base.html")


@app.route('/download/')
def download_link():
    mirror = request.args.get('mirror') 
    book_soup = soup(get(mirror).text,'html.parser')
    down_link = str(book_soup.find("h2").find("a")['href'])
    title = book_soup.find("h1").text.strip()
    wget.download(down_link,out="downloads/"+title.replace(" ",'_'))
    return 'Downloading'

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
