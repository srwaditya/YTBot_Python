from selenium import webdriver
from time import sleep
driver1= webdriver.Chrome(executable_path="/Users/adityashrivastava/Downloads/my_project/chromedriver") ''' Here you put your chromedriver path location '''
driver2= webdriver.Chrome(executable_path="/Users/adityashrivastava/Downloads/my_project/chromedriver")
driver3= webdriver.Chrome(executable_path="/Users/adityashrivastava/Downloads/my_project/chromedriver")

driver1.get("")   '''-- Put here your video URL 1 '''
driver2.get("")   '''-- Put here your video URL 2 '''
driver2.get("")   '''-- Put here your video URL 3 '''

while True:
    sleep(60)
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()
