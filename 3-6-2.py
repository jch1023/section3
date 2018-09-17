import sys
import io
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

firefox_options = Options()
firefox_options.add_argument('--headless') #cli 브라우저를 사용 하지 않고 하는 방법

driver = webdriver.Firefox(firefox_options=firefox_options,executable_path='c:/workspace/section3/webdriver/firefox/geckodriver')
#webdriver.Firefox  앞글자 대문자 나머지 소문자
#driver = webdriver.Chrome('c:/workspace/section3/webdriver/chrome/chromedriver') # 창 켜지면서 보면서 하는거
#driver.set_window_size(1920,1280)
#driver.implicitly_wait(5) #암묵적 5초 대기

driver.get('https://google.com')
#time.sleep(1) #강제 휴식
driver.save_screenshot('c:/f_ch.png')

#driver.implicitly_wait(10)

driver.get('https://naver.com')
#time.sleep(1)
driver.save_screenshot('c:/ff_ch.png')

driver.quit()
print('스크린샷 완료')
