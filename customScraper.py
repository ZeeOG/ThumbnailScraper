from selenium import webdriver
import requests
import os
from selenium.webdriver.common.by import By
from io import BytesIO
from PIL import Image
import base64
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Please use images in your search term when searching


def image_scraper(search_term, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    driver = webdriver.Chrome()
    driver.get("https://google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)

    image_list = []

    image_divs = driver.find_elements(
        By.CSS_SELECTOR, ".gdOPf.uhHOwf.ez24Df")[:11]

    # print(image_divs)
    for i in image_divs:
        pic = i.find_element(By.TAG_NAME, "img")

        src = pic.get_attribute("src")

        image_list.append(src)

    # print(image_list)

    for i, n in enumerate(image_list):
        try:
            if n.startswith("data:image/"):
                base64_data = n.split(",")[1]
                img_data = base64.b64decode(base64_data)
                img = Image.open(BytesIO(img_data))
            else:
                response = requests.get(n)
                img = Image.open(BytesIO(response.content))
            if img.mode != "RGB":
                img = img.convert("RGB")
            img_path = os.path.join(output_folder, f"{search_term}{i}.jpeg")
            img.save(img_path, "JPEG")
        except Exception as e:
            print(f"Failed to process image {i + 1}: {e}")

    driver.quit()


image_scraper("hair images", "hair_images")
