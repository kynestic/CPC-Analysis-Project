# !pip install selenium
# !apt-get update # Update package lists
# !apt-get install -y chromium-chromedriver # Install chromium and chromedriver

from selenium import webdriver
from selenium.webdriver.common.by import By # Import By
from datetime import datetime
import time
import csv
import pandas as pd

page = 1
options = webdriver.ChromeOptions()
options.add_argument('--headless') # Run Chrome in headless mode
options.add_argument('--no-sandbox') # Disable sandbox for security reasons in this environment
driver = webdriver.Chrome(options=options) # Apply options to the driver

res_list = []

while True:
    driver.get(f'https://markets.businessinsider.com/news/nvda-stock?p={page}')
    time.sleep(3)
    ele_list = driver.find_elements(By.CLASS_NAME, 'latest-news__story')

    if page == 194:
        break

    for item in ele_list:
        date_str = item.find_element(By.CSS_SELECTOR, '.latest-news__meta time').get_attribute('datetime')
        
        event_str = item.find_element(By.CLASS_NAME, 'news-link').text

        timestamp = datetime.strptime(date_str, '%m/%d/%Y %H:%M:%S %p')
        timestamp = timestamp.strftime('%Y/%m/%d/')
        res_list.append([timestamp, event_str])

    page += 1

data = pd.DataFrame(res_list, columns=['timestamp', 'events'])

data.to_csv(r'data\raw\stocknews.csv' ,index=False ,encoding='utf-8', header=True)
    
driver.quit()