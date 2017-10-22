from lxml import html
import requests

page = requests.get('https://www.pexels.com/photo/background-blur-botanical-branches-339614/')
tree = html.fromstring(page.content)

author = tree.xpath('//h3[@class="mini-profile__name"]//a/text()')

print 'Autor: ', author
