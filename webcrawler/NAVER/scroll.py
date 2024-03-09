import requests
from bs4 import BeautifulSoup

data = requests.get('https://s.search.naver.com/p/review/47/search.naver?ssc=tab.blog.all&api_type=4&query=%EC%A3%BC%EC%8B%9D&start=31&nx_search_query=&nx_and_query=&nx_sub_query=&ac=0&aq=0&spq=0&sm=tab_hty.top&nso=&prank=37&ngn_country=KR&lgl_rcode=02285104&fgn_region=&fgn_city=&lgl_lat=37.641607&lgl_long=126.770533&enlu_query=IggCAAaCULjWAAAA4HE2fHGDyHsvCfCfv4iI6A1%2FCYiD3CPs%2FteBQMy%2BF4JAEZpZBXe06cRm6RiHZ9np&abt=&_callback=getBlogContents&_callback=getBlogContents&_=1708781492349'
)
soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
for i in range(0,10):
    print(i+1,soup.select('.title_area a')[i].text)