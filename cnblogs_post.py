import requests
from pyquery import PyQuery as pq

url = 'https://www.cnblogs.com/subconscious/p/5058741.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
html = requests.get(url, headers=headers).text
doc = pq(html)
items = doc('.post').items()
for item in items:
    # name = item.find('h1').text()
    title = pq(item.find('.postTitle').html()).text()
    post = pq(item.find('.blogpost-body').html()).text()
    file = open('cnblogspost.txt', 'a', encoding='utf-8')
    file.write('\n'.join([title, post]))
    file.write('\n' + '=' * 50 + '\n')
    file.close()

