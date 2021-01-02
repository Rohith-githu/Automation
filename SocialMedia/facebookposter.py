from selenium import webdriver
import time
import pyautogui
link = input('Enter the link :\n')
post = input('Enter the Post :\n')

# block_notify = 
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
# driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')

login_user = driver.find_element_by_xpath('//*[@id="email"]')
login_password = driver.find_element_by_xpath('//*[@id="pass"]')
login_user.send_keys('sairohith7050@gmail.com')
login_password.send_keys('rohith7050')

login_click = driver.find_element_by_xpath('//*[@id="u_0_b"]')
login_click.click()

time.sleep(9)
writer = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[2]/div[3]')

writer.click()

time.sleep(5)

writer_nav = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[2]/div/div/div[1]/div[2]/div')
writer_nav.click()

time.sleep(5)

writer_info = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div[1]/div/div[1]/div/div/div/div/div[2]/div/div/div/div')
# writer_info.click()
writer_info.send_keys(f'{link}\n{post}')
time.sleep(5)
post_button = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div')
post_button.click()

time.sleep(5)

like_button = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[4]/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]')
like_button.click()

time.sleep(10)
driver.quit()