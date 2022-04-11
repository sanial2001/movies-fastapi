import requests
from bs4 import BeautifulSoup


def new_series_feeds():
    d = {}
    html_text = requests.get("https://moviesdaily.com/discovertvshows").text
    soup = BeautifulSoup(html_text, 'lxml')
    soup.prettify()
    new_series = soup.find_all('div', class_='col-md-8 col-sm-8')
    for new_show in new_series:
        show_name_div = new_show.find('div', class_='col-md-11 col-sm-11 col-xs-11')
        show_name = show_name_div.h4.a.text
        show_details = show_name_div.h4.a['href']
        release_date = show_name_div.h4.span.text
        about = new_show.p.text.replace('\n', '')
        d[show_name] = {}
        d[show_name]['details'] = show_details
        d[show_name]['release_date'] = release_date
        d[show_name]['about'] = about
        # print(movie_name, release_date, about)
    return d
