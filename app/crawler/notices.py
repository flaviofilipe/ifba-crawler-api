import requests
from bs4 import BeautifulSoup

url = 'https://portal.ifba.edu.br/conquista/noticias-2/noticias-campus-vitoria-da-conquista'


def get_dat_publish(article):
    data_modification = article.header.find(class_='documentByLine').getText().replace("  ", "").replace('\n', "")
    date = data_modification[data_modification.find('modificação') + 11:]
    return date


def get_articles(start=1):
    b_start = 0 if start == 1 else 30 * (start - 1)
    page_url = '{}?b_start:int={}'.format(url, b_start)
    page = requests.get(page_url, verify=False)

    # Criar o objeto BeautifulSoup
    soup = BeautifulSoup(page.text, 'html.parser').find_all('article', class_='entry')
    articles = []
    for article in soup:
        summary = article.header.find(class_='summary')
        article = {
            'title': summary.a.getText(),
            'link': summary.a['href'],
            'date': get_dat_publish(article)
        }
        articles.append(article)
    return articles
