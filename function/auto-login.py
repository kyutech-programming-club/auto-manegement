import time
from selenium import webdriver

driver = webdriver.Chrome() # WebDriverのインスタンスを作成
driver.get('https://ict-t.el.kyutech.ac.jp/') # URLを指定してブラウザを開く
time.sleep(2) # 2秒待機
driver.find_element_by_link_text("ログイン").click()
search_box = driver.find_element_by_name('j_username') # name属性で検索ボックスを特定
search_box1 = driver.find_element_by_name('j_password')
search_box.send_keys('aeve2636') # 検索ボックスにテキストを入力
search_box1.send_keys('hg9Xh6Vd')
driver. find_element_by_xpath("//button[text() = 'Login']").click()
time.sleep(2) # 2秒待機
#driver.quit() # ブラウザを閉じる
