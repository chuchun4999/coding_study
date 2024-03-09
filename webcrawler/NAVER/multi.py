import requests
import json
import time

url = [
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1609524000000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608811200000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608098400000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1606672800000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605960000000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605242700000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1604534400000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603821600000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603108800000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1602396000000',
]

def 함수(구멍):
    data = requests.get(구멍)
    딕셔너리 = json.loads(data.content)
    return 딕셔너리['data'][0]['Close']

# 함수(url[0])

# 멀티쓰레딩으로 코드실행시키는 법
# 기본 내장라이브러리를 저렇게 import 해오시고 (멀티쓰레딩하는 법인데 멀티프로세싱을 하려면 .dummy를 제거합니다)
from multiprocessing.dummy import Pool as ThreadPool

pool = ThreadPool(4)
result = pool.map(함수, url) # 동시 처리 가능
pool.close()
pool.join()
print(result)
# ThreadPool() 에다가 몇개의 프로세스/쓰레드로 동시에 작업을 시킬지 숫자로 적으시고
# map 에다가는 저거 적으시면 됩니다. 끝! 
# 그 다음에 마무리되면 close() join() 을 차례로 해주면 됩니다. (작업 고만시키고 작업한거 join 그니까 전부 가져오라는 뜻입니다.)
# 그럼 map()에서 리스트안에 있던 자료들을 전부 함수에 차례로 집어넣어주는데 그 집어넣은 결과를 리스트로 만들어줍니다. 
# 근데 그냥 해주진 않고 멀티쓰레딩을 이용해서 분산처리를 지가 알아서 해준다는 겁니다. 
# 하지만 빨간게 뭔 뜻인지 모르겠으니 다음시간에 map 함수를 알아봅시다. 