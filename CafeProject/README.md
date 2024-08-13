## 상권정보시스템 웹에서 상권정보 보고서 수집
### https://sg.sbiz.or.kr/

***셀레니움***을 활용해서
- 팝업 닫기
- 로그인 (sendkey)
- 버튼 클릭
- 포커스 이동

과 같은 작업들을 자동화하였습니다.

노트북 화면이 작아서 팝업 창의 닫기 버튼이 보이지 않아 요소를 찾아 클릭하는 데 어려움이 있었지만, 자바스크립트 코드를 실행해 문제를 해결할 수 있었습니다.

```
# 팝업 창 닫기
try:
    # 자바스크립트 코드 실행으로 클릭
    close_button = driver.find_element(By.CSS_SELECTOR, '#help_guide > div > div.foot > a')
    driver.execute_script("arguments[0].click();", close_button)
except:
    print("Element not found")
    pass
```

웹 자동화 실행 동영상 링크 :
https://github.com/user-attachments/assets/7fdaba0d-11c1-4d9a-b1a3-e5cd15564ae6

