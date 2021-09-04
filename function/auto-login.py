import time
from selenium import webdriver

driver = webdriver.Chrome() # WebDriverのインスタンスを作成
driver.get(r'file:///C:\Users\subar\Desktop\新しいフォルダー\auto-manegement\site\index.html') # URLを指定してブラウザを開く
time.sleep(2) # 2秒待機
driver. find_element_by_xpath("//input[@id = 'username']").send_keys('三木彪瑠')
time.sleep(1)
driver. find_element_by_xpath("//input[@id = 'password']").send_keys('mikitakeru')
time.sleep(1)
driver. find_element_by_xpath("//button[text() = 'Login']").click()
#driver.find_element_by_link_text("システム工学").click()
#driver.find_elements_by_tag_id("yui_3_17_2_1_1630728402296_179").click()
time.sleep(2) # 2秒待機
driver.find_element_by_link_text("電磁気学Ⅰ(2021):共通:Q01:月曜日4時限木曜日2時限(1)").click()
time.sleep(2)
driver. find_element_by_xpath("//button[text() = '出席']").click()
time.sleep(2)
driver.quit() # ブラウザを閉じる
