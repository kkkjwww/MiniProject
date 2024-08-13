# 모듈 임포트
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import getpass

# 사용자로부터 비밀번호 입력받기
id = getpass.getpass("아이디 : ")
pw = getpass.getpass("비빌번호 : ")

# id = input("아이디 : ")
# pw = input("비빌번호 : ")

# detach 옵션 설정
option = Options()
option.add_experimental_option("detach", True)

# driver 에 옵션 적용
driver = webdriver.Chrome(options=option)
driver.get('https://sg.sbiz.or.kr/')  # 웹 페이지 로드
driver.maximize_window()  # 창 최대화

driver.implicitly_wait(20)

# 팝업 창 닫기
try:
    close_button = driver.find_element(By.CSS_SELECTOR, '#help_guide > div > div.foot > a')
    # 그냥 클릭하면 안되고 자바스크립트로 클릭하면 된다. (명시적 wait도 작동되지 않음.)
    driver.execute_script("arguments[0].click();", close_button)
except:
    print("Element not found")
    pass

time.sleep(2)

# 로그인 버튼
driver.find_element(By.CSS_SELECTOR, '#menu > div.lay.scrollbarView > div > div.head > div > ul > li > a > span').click()  # '로그인' 버튼 클릭


driver.find_element(By.CSS_SELECTOR, '#id').send_keys(id)  # 사용자 아이디
driver.find_element(By.CSS_SELECTOR, '#pass').send_keys(pw)  # 사용자 비밀번호
driver.find_element(By.CSS_SELECTOR, 'body > div > div.l_content > form > div > input').click()  # '로그인' 버튼 누르기

time.sleep(5)

try:
    # 오늘 하루 이 창을 열지 않음 선택자가 계속 바뀌는 문제 해결
    for i in range(12, 51):
        selector = f'#container > div:nth-child({i}) > div > div.head.close-option > div > label:nth-child(2)'
        try:
            # text를 기준으로 원하는 팝업 창을 클릭
            element = driver.find_element(By.CSS_SELECTOR, selector)
            if element.text == '오늘 하루 이 창을 열지않음':
                element.click()
                break
        except:
            continue
    
    # 나머지 팝업 창
    driver.find_element(By.CSS_SELECTOR, '#noticeCloseForever0').click()
    driver.find_element(By.CSS_SELECTOR, '#noticeCloseForever1').click()
    last_popup = driver.find_element(By.CSS_SELECTOR, '#noticeCloseForever2')
    driver.execute_script("arguments[0].click();", last_popup)

except:
    print("Element not found")
    pass


# 상세분석 페이지로 이동. 자바스크립트로 해야 한다.
detail_analyize = driver.find_element(By.CSS_SELECTOR, '#toLink > a > h4')  # '상세분석' 버튼
driver.execute_script("arguments[0].click();", detail_analyize) # 클릭

driver.find_element(By.CSS_SELECTOR, '#container > div:nth-child(1) > div:nth-child(2) > div > div > ul > li:nth-child(2) > label > span').click() # '도로명' 클릭
driver.find_element(By.CSS_SELECTOR, '#searchAddress').send_keys('대구 중구 달구벌대로 2195 경일빌딩')  # 도로명 주소 입력 / 경대병원역 4번 출구 im뱅크
driver.find_element(By.CSS_SELECTOR, '#layerPopAddressMove').click()  # 검색 버튼 클릭

time.sleep(1)  # 검색 결과가 나올 때까지 조금 기다려 줌
driver.find_element(By.CSS_SELECTOR, '#adrsList > li:nth-child(1) > label > span').click()  # 검색 결과가 여러 개인 경우의 첫 번째 검색 결과 선택지
driver.find_element(By.CSS_SELECTOR, '#container > div:nth-child(1) > div:nth-child(3) > div.foot > a:nth-child(2)').click()  # 확인

driver.find_element(By.CSS_SELECTOR, '#upjong > ul > li:nth-child(2) > label').click()  # 음식
driver.find_element(By.CSS_SELECTOR, '#container > div:nth-child(17) > div > div.midd > div.midd > div.searchview.scrollbarView > div > ul > li.best > div > ul > li:nth-child(2) > label > span').click()  # 카페
time.sleep(0.5)  # 0.5초 쉬기
driver.find_element(By.CSS_SELECTOR, '#checkTypeConfirm > span').click()  # 확인

driver.find_element(By.CSS_SELECTOR, '#map > div:nth-child(1) > div > div:nth-child(6) > div:nth-child(2) > div > ul > li.child').click()  # 상권분석

driver.find_element(By.CSS_SELECTOR, '#map > div:nth-child(1) > div > div:nth-child(6) > div:nth-child(2) > div > ul > li.child > div > ul > li:nth-child(2) > label > svg').click()  # 반경
driver.find_element(By.CSS_SELECTOR, '#auto_circle > div > div.midd > ul > li:nth-child(3) > label').click()  # 300미터
driver.find_element(By.CSS_SELECTOR, '#auto_circle > div > div.foot > a:nth-child(2) > span').click()  # 확인

driver.find_element(By.CSS_SELECTOR, '#map > div:nth-child(1) > div > div:nth-child(6) > div:nth-child(3) > img').click()  # 분석

# 저장 버튼 계속 누르고 저장할 수 없으면 확인 버튼 누르고 아니라면 빠져나온다.
while True:
    driver.find_element(By.CSS_SELECTOR, '#printReport').click()
    try:
        driver.switch_to.alert.accept() # 알림창이 나타나면 '확인'을 누르고
        time.sleep(0.5)  # 0.5초를 더 쉼
    except:  # 만약 알림창이 나타나지 않아 '확인'을 누를 수 없는 경우
        break  # 보고서 생성이 완료되었다는 의미이므로 while 문 중단


driver.switch_to.window(driver.window_handles[1])  # 새로 열린 탭으로 포커스를 이동 (pdf)

driver.find_element(By.CSS_SELECTOR, '#OZViewer > div:nth-child(1) > input.oz_ui_layout.btnSAVEAS').click()  # 저장 버튼 클릭
driver.find_element(By.CSS_SELECTOR, 'body > div.ui-dialog.ui-corner-all.ui-widget.ui-widget-content.ui-front.ui-dialog-buttons.ui-draggable.oz_ui_layout > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(2)').click()  # 확인 클릭

time.sleep(10)  # 보고서가 다운로드될 수 있도록 10초간 대기

driver.quit()  # 창 닫기