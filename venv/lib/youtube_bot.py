from selenium import webdriver
from time import sleep
driver1= webdriver.Chrome(executable_path="/Users/adityashrivastava/Downloads/my_project/chromedriver")
driver2= webdriver.Chrome(executable_path="/Users/adityashrivastava/Downloads/my_project/chromedriver")
driver3= webdriver.Chrome(executable_path="/Users/adityashrivastava/Downloads/my_project/chromedriver")

driver1.get("https://www.youtube.com/watch?v=vPIwFPEIJBg")
driver2.get("https://www.youtube.com/watch?v=6-aO3XtI6os")
driver2.get("https://www.youtube.com/watch?v=QLrKXerJAAg")

while True:
    sleep(60)
    driver1.refresh()
    driver2.refresh()
    driver3.refresh()
