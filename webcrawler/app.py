리스트 = ['삼성전자','카카오','네이버','신풍제약']
f = open('data.txt', 'w')
for item in 리스트:
    f.write(item+'\n')
f.close()
f = open('multi.txt', 'w')
for i in range(2,10):
    for j in range(1,10):
        f.write(f'{i*j}\n')
f.close()
