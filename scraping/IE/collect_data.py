from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants.const import INDEED_ALLOW_TAG, INDEED_NEXT_BTN_TAG, INDEED_PAGE_COUNT_TAG, INDEED_SALARIES_TAG, INDEED_TILES_TAG, INDEED_URL, JOBS_ALLOW_TAG, JOBS_NEXT_SUBLINK, JOBS_PAGE_COUNT_TAG, JOBS_SALARIES_TAG, JOBS_URL, JOBS_TILES_TAG



def preSetting(accept_cookies_tag):
    try:
        # Find and click the "Accept All" button
        accept_all_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, accept_cookies_tag ))
        )
        accept_all_button.click()

    except Exception as e:
        print(f"Exception while clicking 'Accept All' button: {e}")
        return None  # or any other value to indicate failure

def getPageCount(page_count_tag):
    try:
        # Find the specified <a> element
        target_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,page_count_tag ))
        )
        aria_label_value = target_link.get_attribute("aria-label")
        parts = aria_label_value.split(" of ")
        n_value_str = parts[1]
        return  int(n_value_str)

    except Exception as e:
        print(f"Exception while locating target link: {e}")
        return None  

def navigateToNextPage(i,max_value, next_sublink) :
        next_page = f"{i} of {max_value}"
        next_link = next_sublink + f'"{next_page}"]'

        target_link = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, next_link ) ))
        target_link.click()

def parseDataByPageCount(job_titles_tag, job_salaries_tag ):
    max_value = getPageCount(JOBS_PAGE_COUNT_TAG)

    for i in range(1,max_value+1):
        try:
            if i != 1 : 
                navigateToNextPage(i,max_value, JOBS_NEXT_SUBLINK)

            job_titles = driver.find_elements(By.XPATH, job_titles_tag )
            job_salaries = driver.find_elements(By.XPATH,job_salaries_tag )

            for i in range(0,len(job_salaries)):
                print(f"{job_titles[i].text} {job_salaries[i].text}")

            time.sleep(2)  

        except Exception as e:
            print(f"Exception: {e}")
            break



def parseDataByNextBtn (job_titles_tag, job_salaries_tag, next_btn_tag ):

    while True:
        try:
            
            next_btn = driver.find_elements(By.XPATH, next_btn_tag )
            job_titles = driver.find_elements(By.XPATH, job_titles_tag )
            job_salaries = driver.find_elements(By.XPATH,job_salaries_tag )

            for i in range(0,len(job_salaries)):
                print(f"{job_titles[i].text} {job_salaries[i].text}")

            if not next_btn: 
                break

            time.sleep(2)  
        

        except Exception as e:
            print(f"Exception: {e}")
            break

driver = webdriver.Chrome()

driver.get(INDEED_URL)

preSetting(INDEED_ALLOW_TAG)
if len(INDEED_PAGE_COUNT_TAG) != 0 : 
    parseDataByPageCount(INDEED_TILES_TAG, INDEED_SALARIES_TAG)
else :
    parseDataByNextBtn(INDEED_TILES_TAG, INDEED_SALARIES_TAG,INDEED_NEXT_BTN_TAG)


# Close the browser
driver.quit()


