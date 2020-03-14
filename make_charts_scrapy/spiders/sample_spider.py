import scrapy

class SampleSpider(scrapy.Spider):
    # crawler name
    name = 'sample'
    # target domain
    allowed_domains = ['google.com']
    # target start crawling url
    start_urls = ['https://www.google.com/?hl=ja']

    def parse(self, response):
        print(response.text)