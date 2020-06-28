import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://lobste.rs/')
soup = BeautifulSoup(res.text, 'html.parser')
lobster_links = soup.select('.u-url')
lobster_subtext = soup.select('.story')


def create_custom_lb_list(links, subtext):
    lb = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        score = subtext[index].select('.score')
        if len(score):
            points = int(score[0].getText())
            if points > 10:
                lb.append({'title': title, 'link': href, 'score': points})
    return sort_stories_by_score(lb)


def sort_stories_by_score(lb_list):
    return sorted(lb_list, key=lambda k: k['score'], reverse=True)


pprint.pprint(create_custom_lb_list(lobster_links, lobster_subtext))
