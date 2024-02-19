JOBS_URL = "https://www.jobs.ie/jobs/nurse/in-ireland?radius=20&searchOrigin=Resultlist_top-search"

JOBS_ALLOW_TAG = '//div[@id="ccmgt_explicit_accept" and @class="privacy-prompt-button primary-button ccmgt_accept_button"]'
JOBS_TILES_TAG = '//div[@class="res-nehv70" and @data-genesis-element="BASE"]'
JOBS_SALARIES_TAG = '//span[@class="res-1vpeoiv" and @data-at="job-item-salary-info"]'
JOBS_NEXT_BTN_TAG = ''
JOBS_PAGE_COUNT_TAG = '//a[@class="res-9hatlb" and @data-genesis-element="BUTTON"]'
JOBS_NEXT_SUBLINK = '//a[@class="res-14ttpod" and @data-genesis-element="BUTTON" and @aria-label='



INDEED_URL = "https://ie.indeed.com/jobs?q=Nurse&l=Ireland"



INDEED_ALLOW_TAG = '//button[@id="onetrust-accept-btn-handler"]'
INDEED_TILES_TAG = '//span[starts-with(@id, "jobTitle")]'
INDEED_SALARIES_TAG = '//div[@data-testid="attribute_snippet_testid" and @class="css-1ihavw2 eu4oa1w0"]'
INDEED_NEXT_BTN_TAG = '//a[@data-testid="pagination-page-next"]'
INDEED_PAGE_COUNT_TAG = ''
INDEED_NEXT_SUBLINK = ''