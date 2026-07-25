from bs4 import BeautifulSoup
import requests
import schedule
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
# url = "https://divar.ir/s/isfahan/real-estate?map_interaction=search_this_area_disabled"
url = "https://divar.ir/s/isfahan/jobs"
driver.get(url)
last_height = driver.execute_script("return document.body.scrollHeight")


file_path = Path(__file__).parent / "job_datas.txt"
f = open(file_path,'w',encoding='utf8')



def details(workss):
    print(len(workss))
    list_details = []
    for work in workss:

        list_test = []
        title = work.find_element(By.CSS_SELECTOR, "h2.kt-post-card__title").text
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
    time.sleep(3)
    new_height = driver.execute_script("return document.body.scrollHeight")
    # works = driver.find_elements(By.CSS_SELECTOR, "div.kt-post-card__info")
    works = driver.find_element(By.CSS_SELECTOR, "div.post-list-eb5625555555")
    print(works.text)
    time.sleep(5)
    works2 = works.find_elements(By.CSS_SELECTOR, "div.post-list__items-container-e44b2")
    works3 = works.find_elements(By.CSS_SELECTOR, "div.widget-col-d2306")
    jobs = details(works3)
    for job in jobs:
        for str in job:
            f.write(str+"\n")
        f.write("\n____________________\n")    

    if last_height == new_height:

        break
    else:
        last_height = new_height











f.close()

