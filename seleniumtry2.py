from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome('chromedriver')
browser.maximize_window()
browser.get("http://www.google.co.in")
windows_before  = browser.current_window_handle
browser.execute_script("window.open('https://www.yahoo.com')")
WebDriverWait(browser, 10).until(EC.number_of_windows_to_be(2))
windows_after = browser.window_handles
new_window = [x for x in windows_after if x != windows_before][0]
browser.switch_to.window(new_window)
