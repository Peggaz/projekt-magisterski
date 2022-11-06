from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import datetime as dt
import pandas as pd

# Opening the connection and grabbing the page
from webdriver_manager.chrome import ChromeDriverManager

my_url = 'https://www.google.com/search?q='+"wig20"
option = Options()
option.headless = False
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(my_url)
driver.maximize_window()

action = webdriver.ActionChains(driver)
search_bar = WebDriverWait(driver,
                           20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/div[1]'
                                                                           '/div[1]/div/div[2]/input')))
search_button = WebDriverWait(driver,
                              20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[2]/'
                                                                              'div[1]/div[3]/center/input[1]')))

search_bar.send_keys('dollar euro')
search_button.click()

element = WebDriverWait(driver,
                              20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[2]/div[9]/div[1]/'
                                                                              'div[2]/div/div[2]/div[2]/div/div/div[1]/'
                                                                              'div/div/div/div/div/div[2]/div/div[2]/div'
                                                                              '/div')))
loc = element.location
size = element.size

print(loc)
print(size)

action.move_to_element_with_offset(element, 301, 0).perform()



date = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]'
                                    '/div/div/div[1]/div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/'
                                    'span[4]').text
value = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/'
                                     'div/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/span[1]').text

limit = dt.datetime.strptime('05/15', '%m/%d')
pace = -5

while True:
    action.move_by_offset(pace, 0).perform()
    date = driver.find_element_by_xpath(
        '/html/body/div[6]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/'
        'div[2]/div/div[2]/div/div/div[1]/span[4]').text
    value = driver.find_element_by_xpath(
        '/html/body/div[6]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/'
        'div[2]/div/div[2]/div/div/div[1]/span[1]').text

    if dt.datetime.strptime(date, '%a, %d %b') < limit:
        break

driver.quit()

dictionary = {}
dictionary[date] = value

limit = dt.datetime.strptime('05/15', '%m/%d')
pace = -5

while True:
    action.move_by_offset(pace, 0).perform()
    date = driver.find_element_by_xpath(
        '/html/body/div[6]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/'
        'div[2]/div/div[2]/div/div/div[1]/span[4]').text
    value = driver.find_element_by_xpath(
        '/html/body/div[6]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/'
        'div[2]/div/div[2]/div/div/div[1]/span[1]').text

    if dt.datetime.strptime(date, '%a, %d %b') < limit:
        break

    if date in dictionary:
        pass
    else:
        dictionary[date] = value

driver.quit()

df = pd.DataFrame.from_dict(dictionary, orient='index')