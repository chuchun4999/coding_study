# nunu = { 
#     'q': 'eat',
#     'w': 'snowball'
# }
# garen = { 
#     'q': 'strike',
#     'w': 'courage'
# }

#오브젝트 한줄컷 생산해주는 기계
class Hero():
    def __init__(self, 구멍):
        self.q = 구멍
        self.w = ''
    
    def hello(self):
        print('안녕하세요')
        
nunu = Hero('eat','snowball')
garen = Hero('strike','courage')
print(nunu.q)
print(nunu.e)