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
f = open(file_path,'a',encoding='utf8')



def details(works):
    for work in works:
        list = []
        title = work.find_element(By.CSS_SELECTOR, "div.kt-post-card__title").text
        price = work.find_element(By.CSS_SELECTOR, "div.kt-post-card__description").text
        pey_model = work.find_element(By.CSS_SELECTOR, "div.kt-post-card__description").text
        location = work.find_element(By.CSS_SELECTOR, "div.kt-post-card__bottom span.kt-post-card__bottom-description").text

        list.append(title, price, pey_model, location)
        return list



while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")

    works = driver.find_elements(By.CSS_SELECTOR, "div.kt-post-card__info")
    for i in works:
        print(i.text)
    det = details(works)
    f.write(det)

    if last_height == new_height:
        break
    else:
        last_height = new_height




f.close()







# soup = bs4.BeautifulSoup(html,"html.parser")




# import requests

# res = requests.get("https://divar.ir/s/isfahan/jobs")


# print(res.text)





























