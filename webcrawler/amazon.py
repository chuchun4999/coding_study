import requests

헤더스 = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
쿠키 = {
    'session-id':'133-3828461-3490119',
    'session-id-time':'2082787201l',
    'i18n-prefs':'USD',
    'lc-main':'ko_KR',
    'sp-cdn':'L5Z9:KR',
    'skin':'noskin', 'ubid-main':'135-3225956-9984849', 'session-token':'oHRtYF6EqesvWJiVUL+OSuaQrXZ/l3kQ79JtLzQoZqOmFNxTB1SsokXUofAyrn9VUfGK3m1kGqpb+65XB1wSMA6GlePz+SF+QmHSW3ihGHWTLwQ9lHQ7StkcFuHyZlGh2QS6SI17SMRbc8Nnr4es87rqD4XPuuQqHly50vI/N7hc9YZvKyFbxZMgHrhsfIoV2evPaaBYpA9qC6BGzenl6mYiOsdI7L1TEV5qpijQRt54jHQrLeHzeUO4unSQrEJZdzDFrXeOyfBl4th2nDi+MDlfwy7xuYPpf8K2JYr1zN+ICGamIwU3dGbvpcZFkgFzznnNL5m9henFk4LBT/4thOu/KziSWuHZ', 'csm-hit:tb':'7PD41WA4PVGXNESVRASJ+s-JBZXD4T8ZJDREV3TSYFR|1710252993268&t:1710252993268&adb:adblk_no'
}
r = requests.get('https://www.amazon.com/s?k=monitor&crid=368L5QH87WP62&sprefix=monit%2Caps%2C249&ref=nb_sb_noss_2', headers=헤더스, cookies=쿠키 )
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.select('.a-size-medium')[0])

# 에러시 프로그램 정지를 방지 
try:
    print(soup.select('.a-size-medium')[110])
except:
    print('안되네요')

# if(r.status_code) == 200:
#     print(soup.select('.a-size-medium')[0])
# else:
#     print('에러났어요')

# print(r.content)
# print(r.status_code)