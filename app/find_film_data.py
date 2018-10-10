from bs4 import BeautifulSoup
import requests

def get_img_src(query):
    url = """https://www.google.com/images?q='%s'""" % query
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text)
    first_img = soup.find('img')
    src = first_img.get('src')
    return src

def get_imdb_src(query):
    url = """https://www.google.com/search?q='%s imdb'""" % query
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text)
    elements = soup.select('.r a')
    src = elements[0].get('href')[7:]
    link = src.split('&')[0]
    return link

if __name__ == '__main__':
    print(get_imdb_src('shawshank redemption'))