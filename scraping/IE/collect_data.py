from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def preSetting():

    try:
        # Find and click the "Accept All" button
        accept_all_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@id="ccmgt_explicit_accept" and @class="privacy-prompt-button primary-button ccmgt_accept_button"]'))
        )
        accept_all_button.click()

    except Exception as e:
        print(f"Exception while clicking 'Accept All' button: {e}")
        return None  # or any other value to indicate failure

def getPageCount():
    try:
        # Find the specified <a> element
        target_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@class="res-9hatlb" and @data-genesis-element="BUTTON"]'))
        )
        aria_label_value = target_link.get_attribute("aria-label")
        parts = aria_label_value.split(" of ")
        n_value_str = parts[1]
        return  int(n_value_str)

    except Exception as e:
        print(f"Exception while locating target link: {e}")
        return None  

def navigateToNextPage(i,max_value) :
        next_page = f"{i} of {max_value}"
        next_link = f'//a[@class="res-14ttpod" and @data-genesis-element="BUTTON" and @aria-label="{next_page}"]'

        target_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,next_link ))
        )

        target_link.click()

# Specify the URL of the website you want to scrape
url = "https://www.jobs.ie/jobs/nurse/in-ireland?radius=20&searchOrigin=Resultlist_top-search"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

driver.get(url)

preSetting()
max_value = getPageCount()

for i in range(1,max_value+1):
    try:
        if i != 1 : 
            navigateToNextPage(i,max_value)

        job_titles = driver.find_elements(By.XPATH, '//div[@class="res-nehv70" and @data-genesis-element="BASE"]')
        job_salaries = driver.find_elements(By.XPATH, '//span[@class="res-1vpeoiv" and @data-at="job-item-salary-info"]')
        print(f"{len(job_titles)} {len(job_salaries)}")

        for i in range(0,len(job_titles)):
            print(f"{job_titles[i].text} {job_salaries[i].text}")

        time.sleep(2)  

    except Exception as e:
        print(f"Exception: {e}")
        break


# Close the browser
driver.quit()


