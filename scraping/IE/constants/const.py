from models.Job import Job

job_websites = [
    Job(
        url="https://ie.indeed.com/jobs?q=Nurse&l=Ireland",
        cookies_allow_tag='//button[@id="onetrust-accept-btn-handler"]',
        title_tag='//span[starts-with(@id, "jobTitle")]',
        salary_tag='//div[contains(@class, "salary-snippet-container")]',
        next_page_btn_tag='//a[@data-testid="pagination-page-next"]',
        page_count_tag='',
        next_page_sublink_tag='',
        pop_dialog_close_btn_tag='//button[@aria-label="close" and @type="button"]'
    ),
    Job(
        url="https://www.jobs.ie/jobs/nurse/in-ireland?radius=20&searchOrigin=Resultlist_top-search",
        cookies_allow_tag='//div[@id="ccmgt_explicit_accept" and @class="privacy-prompt-button primary-button ccmgt_accept_button"]',
        title_tag='//div[@class="res-nehv70" and @data-genesis-element="BASE"]',
        salary_tag='//span[@class="res-1vpeoiv" and @data-at="job-item-salary-info"]',
        next_page_btn_tag='//a[@data-testid="pagination-page-next"]',
        page_count_tag='//a[@class="res-9hatlb" and @data-genesis-element="BUTTON"]',
        next_page_sublink_tag='//a[@class="res-14ttpod" and @data-genesis-element="BUTTON" and @aria-label=',
        pop_dialog_close_btn_tag=''
    )
]
