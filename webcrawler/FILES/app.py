import os

파일들 = os.listdir(r'/workspaces/coding_study/webcrawler/FILES/test')

print(파일들)

os.path.join('경로', '경로2') # 경로 합치기 함수
os.getcwd() # 현재경로 알려주는 함수

# for i in os.listdir('test'):
#     os.rename(f'test/{i}', f'test/a{i}')

# import shutil
# for i in os.listdir('test'):
#     shutil.copy(f'test/{i}', f'test2/{i}')