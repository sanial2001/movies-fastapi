import requests
from bs4 import BeautifulSoup


def new_movies_feeds():
    d = {}
    html_text = requests.get("https://moviesdaily.com/discovermovies").text
    soup = BeautifulSoup(html_text, 'lxml')
    soup.prettify()
    new_movies = soup.find_all('div', class_='col-md-8 col-sm-8')
    for new_movie in new_movies:
        movie_name_div = new_movie.find('div', class_='col-md-11 col-sm-11 col-xs-11')
        movie_name = movie_name_div.h4.a.text
        movie_details = movie_name_div.h4.a['href']
        release_date = movie_name_div.h4.span.text
        about = new_movie.p.text.replace('\n', '')
        d[movie_name] = {}
        d[movie_name]['details'] = movie_details
        d[movie_name]['release_date'] = release_date
        d[movie_name]['about'] = about
        # print(movie_name, release_date, about)
    return d
