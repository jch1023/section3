import sys
import io
import requests, json
from bs4 import BeautifulSoup


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


#로그인 유저정보
LOGIN_INFO = {
    'user_id':'jch1023',
    'user_pw':'!jeongch7'
}

#Session 생성, with 구문 유지
with requests.Session() as s:
    login_req = s.post('https://user.ruliweb.com/member/login_proc',data=LOGIN_INFO)

    print('login_req',login_req.text)
    print('headers',login_req.headers)
