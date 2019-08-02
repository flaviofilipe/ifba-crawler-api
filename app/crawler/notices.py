
import requests
from bs4 import BeautifulSoup

url = 'https://portal.ifba.edu.br/conquista/noticias-2/noticias-campus-vitoria-da-conquista'

def get_dat_publish(article):
    dataModification = article.header.find(class_='documentByLine').getText().replace("  ", "").replace('\n', "")
    date = dataModification[dataModification.find('modificação')+11:]
    return date

def get_articles(start=1):
    b_start = 0 if start == 1 else 30*(start-1)
    page_url = '{}?b_start:int={}'.format(url, b_start)
    page = requests.get(page_url)

    # Criar o objeto BeautifulSoup
    soup = BeautifulSoup(page.text, 'html.parser').find_all('article', class_='entry')
    articles = []
    for article in soup:
        sumary = article.header.find(class_='summary')
        article = {
            'title' : sumary.a.getText(),
            'link' : sumary.a['href'],
            'date' : get_dat_publish(article)
        }
        articles.append(article)
    return articles

print(get_articles(0))

    