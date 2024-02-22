from dataclasses import dataclass

@dataclass
class Job:
    url: str 
    cookies_allow_tag: str
    title_tag: str
    salary_tag: str
    next_page_btn_tag: str
    page_count_tag: str
    next_page_sublink_tag: str
    pop_dialog_close_btn_tag: str


