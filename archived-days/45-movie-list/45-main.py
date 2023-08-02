from bs4 import BeautifulSoup
import requests
import html

# response = requests.get('https://news.ycombinator.com/news')
response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')

empire_list = response.text

soup = BeautifulSoup(empire_list, 'html.parser')

movie_tags = soup.find_all(name='h3', class_='title')

movie_titles = [html.escape(movie.getText()) for movie in movie_tags][::-1]

for tag in movie_titles:
    print(tag)

# with open('movies.txt', mode='w') as file:
#     for movie in movie_titles:
#         file.write(f'{movie}\n')



# yc_webpage = response.text
#
# soup = BeautifulSoup(yc_webpage, 'html.parser')
#
# article_titles = []
# article_tags = soup.select('.titleline')
#
# print(type(article_tags[0].string))
#
# print(article_tags[0].find(name='a'))
#
# for tag in article_tags:
#     # print(tag.find(name='a').string)
#     article_titles.append(tag.find(name='a').string)
#
# print(article_titles)

# print(article_tag.get('href'))

# print(soup.select_one('.score').string)




# with open('website.html') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# print(soup.title)
#
# print(soup.p)
#
# all_a_tags = soup.find_all(name='a')
#
# for tag in all_a_tags:
#     print(tag.get('href'))
