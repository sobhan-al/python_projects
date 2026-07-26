from bs4 import BeautifulSoup
import requests
import schedule
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
url = "https://divar.ir/s/isfahan/jobs"
driver.get(url)
last_height = driver.execute_script("return document.body.scrollHeight")


f = open("job_datas.txt",'w',encoding='utf8')


job_counter = 0

def details(jobs):
    global job_counter
    print(len(jobs))
    
    list_details = []
    for work in jobs:

        list_test = []
        job_counter+=1
        title = str(job_counter)+"."+work.find_element(By.CSS_SELECTOR, "h2.kt-post-card__title").text
        list_test.append(title)
        price = work.find_elements(By.CSS_SELECTOR, "div.kt-post-card__description")
        for i in price:
            list_test.append(i.text)
        location = work.find_element(By.CSS_SELECTOR, "div.kt-post-card__bottom span.kt-post-card__bottom-description").text
        list_test.append(location)

        list_details.append(list_test)

    return list_details

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)
    new_height = driver.execute_script("return document.body.scrollHeight")

    works = driver.find_elements(By.CSS_SELECTOR, "div.widget-col-d2306")
    jobs = details(works)
    for job in jobs:
        for text in job:
            f.write(text+"\n")
        f.write("\n____________________________\n\n")    

    if last_height == new_height:   
        try: 
            # button = driver.find_element(By.CSS_SELECTOR, "div.post-list__bottom-container-cac2f")
            button = driver.find_element(By.CSS_SELECTOR, "button.kt-button.kt-button--primary.kt-button--outlined.post-list__load-more-btn-be092")
            button.click()
            last_height = new_height
        except:
            break
    else:
        last_height = new_height











f.close()

