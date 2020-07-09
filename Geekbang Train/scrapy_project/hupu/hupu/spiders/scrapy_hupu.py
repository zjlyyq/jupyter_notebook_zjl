import scrapy


class ScrapyHupuSpider(scrapy.Spider):
    name = 'scrapy_hupu'
    allowed_domains = ['hupu.com']
    start_urls = ['https://bbs.hupu.com/bxj-postdate-1']

    def parse(self, response):
        print(response.text)
#         pass
