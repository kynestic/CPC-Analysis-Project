import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import pandas as pd
page = 1
options = webdriver.ChromeOptions()
options.add_argument('--headless') # Run Chrome in headless mode
options.add_argument('--no-sandbox') # Disable sandbox for security reasons in this environment
driver = webdriver.Chrome(options=options) # Apply options to the driver

res_list = []
count = 1
driver.get(r'https://finance.yahoo.com/quote/NVDA/history/?period1=917015400&period2=1728624531')
ele_list = driver.find_elements(By.TAG_NAME, 'tr')
stop = False

limit_date = datetime.strptime('2016/09/28', '%Y/%m/%d')
for row in ele_list:
    items = row.find_elements(By.TAG_NAME, 'td')

    item_list = []
    date = True
    item_count = 1
    for item in items:
        if date:
            text = item.text
            new_date = datetime.strptime(text, r'%b %d, %Y')

            if (new_date < limit_date):
                stop = True
                
            text = new_date.strftime('%Y/%m/%d')


            date = False

            item_list.append(text)
            item_count += 1
            continue
        if item_count == 7:
            volume_list = item.text.split(',')
            total = 0
            for i in range(len(volume_list)):
                total += (10**((len(volume_list) - i - 1)*3))*int(volume_list[i])
            item_list.append(total)
            continue

        item_count += 1
        item_list.append(item.text)
    if stop:
        break    
    res_list.append(item_list)
    count += 1

    
data = pd.DataFrame(res_list, columns=['date', 'open', 'high', 'low', 'close', 'Adj close', 'volume'])
data.to_csv(r'data\raw\stockPrice.csv', index=False, header=True, encoding='utf-8')
driver.quit()