import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get(f'https://news.ycombinator.com/news?p=1')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titlelink')
subtext = soup.select('.subtext')


def parser(r, s, l, sub, num):
    num += 1
    r = requests.get(f'https://news.ycombinator.com/news?p={num}')
    s = BeautifulSoup(r.text, 'html.parser')
    l = s.select('.titlelink')
    sub = s.select('.subtext')
    return r, s, l, sub, num


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(res, soup, links, subtext):
    hn = []
    pg = 1
    while pg != 38:

        for index, item in enumerate(links):
            title = item.getText()
            href = item.get('href', None)
            vote = subtext[index].select('.score')
            if len(vote):
                points = int(vote[0].getText().replace(' points', ''))
                if points > 99:
                    hn.append({'title': title, 'link': href, 'votes': points})
        res, soup, links, subtext, pg = parser(res, soup, links, subtext, pg)

    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(res, soup, links, subtext))
