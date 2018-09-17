import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#r = requests.get('https://api.github.com/events')
#r.raise_for_status() #오류 나는 상황을 오류 메세지로 알려줌
#print(r.text)

jar = requests.cookies.RequestsCookieJar()
jar.set('name', 'kim', domain='httpbin.org',path='/cookies')

#r = requests.get('http://httpbin.org/cookies',cookies=jar)
#r.raise_for_status()
#print(r.text)

#r = requests.get('https://github.com',timeout=5) #5초
#print(r.text)

#r = requests.post('http://httpbin.org/post', data={'name':'kim'}, cookies=jar)
#print(r.text)

payload = {'key1': 'value1', 'key2': 'value2'}
payload2 = (('key1','value1'), ('key2','value2'))
payload3 = {'some':'nice'}

#r = requests.post('http://httpbin.org/post', data=payload1) #form
#print(r.text)

r = requests.post('http://httpbin.org/post', data=json.dumps(payload3)) #json
print(r.text)
