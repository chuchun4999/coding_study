import requests
import json
import time

data = requests.get('https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/ETH?lastDt=1707346800000&interval=1H&1708783687491')
딕셔너리 = json.loads(data.content)
print(딕셔너리['body']['candles'][0]['close'])
시간 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(딕셔너리['body']['candles'][-1]['dt']/1000))
print(시간)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1707346800000/1000)))
print(time.localtime(time.strptime('2024-02-23 23:00:00','%Y-%m-%d %H:%M:%S')))