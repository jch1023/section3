import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#chrome_options = Options()
#chrome_options.add_argument('--headless') #cli 브라우저를 사용 하지 않고 하는 방법
#driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='c:/workspace/section3/webdriver/chrome/chromedriver')

class NcafeWriteAtt:
    #초기화 실행(webdriver 설정)
    def __init__(self):
        self.driver = webdriver.Chrome("c:/workspace/section3/webdriver/chrome/chromedriver")
        self.driver.implicitly_wait(5)

    #네이버 카페 로그인 && 출석 체크
    def writeAttendCheck(self):
        self.driver.get('https://www.naver.com/')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="account"]/div/a/i').click()
        time.sleep(1)
        self.driver.find_element_by_name('id').send_keys('mcverse')
        time.sleep(1)
        self.driver.find_element_by_name('pw').send_keys('!jeongch7')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        time.sleep(1)
        self.driver.get('https://cafe.naver.com/AttendanceView.nhn?search.clubid=15629579&search.menuid=6')
        time.sleep(5)
        self.driver.switch_to_frame('cafe_main')
        self.driver.find_element_by_id('cmtinput').send_keys('반갑습니다!!^^*.')
        self.driver.find_element_by_xpath('//*[@id="main-area"]/div[3]/div[2]/form/fieldset/div/button').click()
        time.sleep(3)

    # 소멸자
    def __del__(self):
        #self.driver.close() #현재 실행 포커스 된 영역을 종료
        self.driver.quit()  #Seleninum 전체 프로그램 종료
        print("Removed driver Object")

#실행

if __name__ == '__main__':
    #객체 생성
    a = NcafeWriteAtt()
    #시작 시간
    start_time = time.time()
    #프로그램 실행
    a.writeAttendCheck()
    #종료 시간 출력
    print("---Total %s seconds ---" % (time.time() - start_time))
    #객체 소멸
    del a
