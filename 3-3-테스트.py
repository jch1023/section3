import sys
import io
import requests

#Rest : POST보내는거, GET받는거, PUT:UPDATE, REPLACE (FETCH : UPDATE, MODIFY), DELETE
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

requests.addheaders(name="key", value="806b6d3f8a26cbfe7aa8c2167f318c46")
r= requests.get('http://api.11st.co.kr/rest/prodmarketservice/prodmarket/2164982298')
print(r.text)


#<Argument name="key" value="806b6d3f8a26cbfe7aa8c2167f318c46"/>
#<Argument name="apiCode" value="ProductSearch"/>
#<Argument name="keyword" value="test"/>
