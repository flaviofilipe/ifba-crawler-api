import requests
from bs4 import BeautifulSoup

from src.contexts.integration.ifba.data.ports.client.http_port import HttpPort


class HttpAdapter(HttpPort):
    def get_posts(self, page_url: str, verify: bool):
        page = requests.get(page_url, verify=verify)

        soup = BeautifulSoup(page.text, 'html.parser').find_all('article', class_='entry')
        posts = []
        for article in soup:
            summary = article.header.find(class_='summary')
            article = {
                'title': summary.a.getText(),
                'link': summary.a['href'],
                'date': self.__get_dat_publish(article)
            }
            posts.append(article)
        return posts

    def __get_dat_publish(self, article):
        data_modification = article.header.find(class_='documentByLine').getText().replace("  ", "").replace('\n', "")
        date = data_modification[data_modification.find('modificação') + 11:]
        return date
