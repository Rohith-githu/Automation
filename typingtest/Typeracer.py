from selenium import webdriver
import pyautogui, time

driver = webdriver.Chrome()
driver.get('https://play.typeracer.com/')
time.sleep(10)

pyautogui.hotkey('ctrl','alt','i')
time.sleep(2)

text = driver.find_element_by_class_name('gameView').text
text = text.split('\n')

print(text[-3])
time.sleep(14)
pyautogui.typewrite(text[-3], interval = 0.05)

time.sleep(15)
driver.quit()