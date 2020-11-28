from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

import csv

# Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("window-size=1400,600")
driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)

# Open url
driver.get("https://www.duunitori.fi")

# Define search parameters
keywords = "Selenium"
location = "Helsinki"

# Get input elements used to search with
search_input = driver.find_element_by_xpath('//*[@id="search-autocomplete"]/ul/li/input')
location_input = driver.find_element_by_xpath('//*[@id="area-autocomplete"]/ul/li/input')

# Execute search with the given keywords/location
search_input.clear()
search_input.send_keys(keywords)

location_input.clear()
location_input.send_keys(location)

location_input.send_keys(Keys.RETURN) # Press Enter

# Wait until the page is loaded
WebDriverWait(driver, 3).until(
    expected_conditions.presence_of_element_located(
        (By.CLASS_NAME, 'gtm-search-result')
    )
)

# Get a list of results
search_results = driver.find_element_by_xpath('/html/body/div[8]/div/div[1]/div[1]/div[1]').find_elements_by_class_name('grid--middle')

# Loop through the result elements and collect the needed information
result_rows = []
for result in search_results:
    title = result.find_element_by_class_name('job-box__title').get_attribute('innerHTML')
    date = result.find_element_by_class_name('job-box__job-posted').get_attribute('innerHTML')
    url = result.find_element_by_css_selector("a").get_attribute("href")
    
    row = {'Title':title, 'DatePosted':date, 'URL':url}
    result_rows.append(row)

# Write results to a CSV file
with open('search_results.csv', mode='w') as csv_file:
    field_names = ['Title', 'DatePosted', 'URL']
    writer = writer = csv.DictWriter(csv_file, fieldnames=field_names)
    writer.writeheader()
    for row in result_rows:
        writer.writerow(row)

# Close Browser
driver.quit()