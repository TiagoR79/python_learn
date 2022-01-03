from selenium import webdriver
from selenium.webdriver.chrome.service import Service

url = "https://www.youtube.com/c/KalleHallden/videos"

service = Service(executable_path="./chromedriver")
browser = webdriver.Chrome(service=service)

browser.get(url)
'''needed for consent - clicks agree button'''
browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div/div/button').click()
'''opens video - click video title'''
browser.find_element_by_xpath('//*[@id="video-title"]').click()
'''

'''
