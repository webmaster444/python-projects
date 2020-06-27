from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get(
    'https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert chrome_browser.title

show_msg_button = chrome_browser.find_element_by_class_name('btn-default')

assert 'Show Message' in chrome_browser.page_source

input_id = chrome_browser.find_element_by_id('user-message')
input_id.clear()
input_id.send_keys('I am extra coool')

show_msg_button.click()

chrome_browser.quit()
