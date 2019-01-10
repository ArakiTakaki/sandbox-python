import requests
from bs4 import BeautifulSoup

# 参考サイト - qiita @matsu0228
# python3でwebスクレイピング(Beautiful Soup)
# https://qiita.com/matsu0228/items/edf7dbba9b0b0246ef8f


target_url = 'https://google.co.jp'
r = requests.get(target_url)  # requestsを使って、webから取得
soup = BeautifulSoup(r.text, 'lxml')  # 要素を抽出

for a in soup.find_all('a'):
    print(a.get('href'))  # リンクを表示
