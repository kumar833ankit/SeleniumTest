#from selenium import webdriver
#driver = webdriver.Chrome(executable_path="D:\python\AI1\chromedriver.exe")

#driver.maximize_window()

#driver.get("https://www.tutorialspoint.com/index.htm")

#driver.refresh()

#driver.close()

from selenium import webdriver


search_string = input("Input the URL or string you want to search for:")

search_string = search_string.replace(' ', '+')



browser = webdriver.Chrome('chromedriver')
browser.maximize_window()



for i in range(1):

	matched_elements = browser.get("https://www.google.com/search?q=" +
									search_string + "&start=" + str(i))

  






             
                          
browser.execute_script("window.open('');")
  
           
browser.switch_to.window(browser.window_handles[1])
matched_element =  browser.get("http://www.youtube.com/search?q=" + 
                                search_string + "&start=" + str(i))

































#results = webadriver.find_elements_by_xpath('//div[@class="r"]/a/h3')  # finds webresults
#results[0].click()# clicks the first one
#webdriver.get(webdriver.find_element_by_class_name("iUh30").text)
###################################################################################################################







from tkinter import * #import tkinter
from tkinter import messagebox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


search_string = input("Input the URL or string you want to search for:")

search_string = search_string.replace(' ', '+')

def tell_weather() :
        browser =  webdriver.Chrome(r'C:\Users\B&O\Downloads\chromedriver11111.exe')


browser = webdriver.Chrome('chromedriver')
browser.maximize_window()
browser2 = webdriver.Chrome('chromedriver')
browser2.maximize_window()
browser3 = webdriver.Chrome('chromedriver')
browser3.maximize_window()

for i in range(1):

	matched_elements = browser.get("https://www.google.com/search?q=" +
									search_string + "&start=" + str(i))

#browser.findElement(By.id("rso")).findElements(By.xpath("/*")).get(0).click();                                   
#browser.find_element_by_css_selector("div.r a h3").click()
#browser.find_element_by_xpath('(//div[@class="r"]/a)[1]').click()
#results = browser.find_elements_by_xpath('//div[@class="r"]/a/h3')  # finds webresults
#results[0].click()

#browser.get(driver.find_element_by_class_name("iUh30").text) 
#result.find_element_by_xpath("./div/h3/a").click() 



browser.set_window_size(480, 320)
browser.set_window_position(480, 320)




matched_element =  browser2.get("http://www.youtube.com/search?q=" + 
                                search_string + "&start=" + str(i))


browser2.set_window_size(480, 320)
browser.set_window_position(480, 320)

matched_element =  browser3.get("http://www.infoplease.com/search?q=" + 
                                search_string + "&start=" + str(i))


browser3.set_window_position(480, 320)
browser3.set_window_size(480, 320)


https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python

if __name__ == "__main__" :
      # Create a GUI window
    root  = Tk()
  
    # set the name of tkinter GUI window
    root.title("Weather App")
  
    # Set the background colour of GUI window 
    root.configure(background = "grey")
  
    # Set the configuration of GUI window 
    root.geometry("425x175")
    root.resizable(0,0) 
    root.minsize(425, 175)
    root.maxsize(425, 175)
  
    # Create a Weather Gui Application label 
    headlabel = Label(root, text = "Weather Gui Application",
                      fg = 'white', bg = 'green')

button1 = Button(root, text = "Scrape Data", bg = "black", 
                     fg = "red", command = tell_weather)