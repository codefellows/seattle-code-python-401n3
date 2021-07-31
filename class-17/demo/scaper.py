import requests
from bs4 import BeautifulSoup

URL = 'https://testing-www.codefellows.org/courses/code-400/'
page = requests.get(URL)
# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup)

results = soup.find(class_='course-details')
# print(results.prettify())

titles = results.find_all('h3')
# print(titles)

# for title in titles:
#     print(title.text)

anchors = results('a')
# print(anchors)

links = [anchor['href'] for anchor in anchors]

# print(links)

python_link = links[3]
link_content = requests.get('https://testing-www.codefellows.org' + python_link)

# print(link_content.content)

link_soup = BeautifulSoup(link_content.content, 'html.parser')


article = link_soup('article')[1]

# print(article)

list_items = article.select('ul li ul li')
# print(list_items)

for li in list_items:
    print(li.text)