import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy import Request
import time

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = ['https://www.jobs.ie/jobs/nurse/in-ireland?radius=20&searchOrigin=Resultlist_top-search']
    
    custom_settings = {
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'DOWNLOAD_DELAY': 2,
    'DEFAULT_REQUEST_HEADERS': {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en',
        'Referer': 'https://www.google.com/',
      }
    }


    def parse(self, response):
        print(response.text)
        
        # You can continue your parsing logic here

# Run the spider
process = CrawlerProcess()
process.crawl(MySpider)
process.start()
