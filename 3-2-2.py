import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#Response 상태 코드
s = requests.Session()
r = s.get('http://httpbin.org/get')
#print(r.status_code)
#print(r.ok)


#https://jsonplaceholder.typicode.com

r = s.get('https://jsonplaceholder.typicode.com/posts/1')
#print(r.text)
#json 활용 메소드
print(r.json().keys())
print(r.json().values())
print(r.encoding) #utf-8 확인
print(r.content) # 컨텐츠를 바이너리 형태로 제공
print(r.raw) #로우 데이터로 제공
