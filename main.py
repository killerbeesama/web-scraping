from bs4 import BeautifulSoup
import requests

r = requests.get("https://news.ycombinator.com/")
data = r.text

soup = BeautifulSoup(data,"html.parser")
point = soup.findAll(name='span',class_='score')
link = soup.findAll(name='a',class_='titlelink')

score = []
for i in point:
    score.append(int(i.get_text().split()[0]))

highest_score_news = max(score)
high_score = score.index(highest_score_news)

link_title = link[high_score].get_text()
goto_link = link[high_score]['href']

print(link_title)
print(goto_link)