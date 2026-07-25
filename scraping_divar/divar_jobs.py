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


file_path = Path(__file__).parent / "home_datas.txt"
f = open(file_path,'w',encoding='utf8')



def details(workss):
    for work in workss:
        list_details = []
        title = work.find_element(By.CSS_SELECTOR, "h2.kt-post-card__title").text
        list_details.append(title)
        price = work.find_elements(By.CSS_SELECTOR, "div.kt-post-card__description")
        for i in price:
            list_details.append(i.text)
        location = work.find_element(By.CSS_SELECTOR, "div.kt-post-card__bottom span.kt-post-card__bottom-description").text
        list_details.append(location)

        return list_details



while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(7)
    new_height = driver.execute_script("return document.body.scrollHeight")
    # works = driver.find_elements(By.CSS_SELECTOR, "div.kt-post-card__info")
    works = driver.find_element(By.CSS_SELECTOR, "div.post-list-eb562")

    works2 = works.find_elements(By.CSS_SELECTOR, "div.post-list__items-container-e44b2")

    jobs = details(works2)
    for job in jobs:
        f.write(job+"\n")
        time.sleep(5)
    f.write("\n")    
    if last_height == new_height:
        break
    else:
        last_height = new_height

    f.write("mioooooooooooooooooooooo")    




f.close()
































