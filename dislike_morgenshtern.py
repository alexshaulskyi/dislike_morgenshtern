import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

load_dotenv()

p = os.getenv('p')
usname = os.getenv('usname')
pw = os.getenv('password')

browser = webdriver.Chrome(p)

# Login through 3rd party services in order to bypass google "We can't sign you in" issue 
browser.get('https://stackoverflow.com')
browser.maximize_window()
time.sleep(4)
browser.find_element_by_xpath('//*[@class = "login-link s-btn s-btn__filled py8 js-gps-track"]').click()
time.sleep(4)
browser.find_element_by_xpath('//*[@class = "grid--cell s-btn s-btn__icon s-btn__google bar-md ba bc-black-3"]').click()
browser.find_element_by_xpath('//input[@type = "email"]').send_keys(usname)
time.sleep(4)
browser.find_element_by_xpath('//button[@class = "VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc"]').click()
time.sleep(4)
browser.find_element_by_xpath('//input[@type = "password"]').send_keys(pw)
browser.find_element_by_xpath('//button[@class = "VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc"]').click()

time.sleep(4)
browser.get('https://www.youtube.com')

search_bar = browser.find_element_by_xpath('//input[@id = "search"]')
search_bar.send_keys('Моргенштерн')
search_bar.send_keys(Keys.RETURN)

browser.find_element_by_xpath('//*[contains(text(), "Фильтры")]').click()
browser.find_element_by_xpath('//*[contains(text(), "За последний час")]').click()

time.sleep(5)

a_elems = browser.find_elements_by_xpath('//a[@class = "yt-simple-endpoint style-scope ytd-video-renderer"]')

titles = []

for elem in a_elems:

    if len(titles) < 10:

        title = elem.get_attribute('title')
        
        if '"' not in title:
            titles.append(title)
        else:

            pass
    
    else:

        break

for title in titles:

    browser.find_element_by_xpath(f'//a[@title = "{title}"]').click()
    time.sleep(5)
    dislike = browser.find_element_by_xpath('//*[contains(@aria-label, "Видео не понравилось")]')
    time.sleep(2)
    status = dislike.get_attribute('aria-pressed')

    if status == 'false':

        dislike.click()
        time.sleep(2)
        browser.back()
        time.sleep(2)
    
    else:

        time.sleep(2)
        browser.back()
        time.sleep(2)