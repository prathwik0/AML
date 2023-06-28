import scrapy


class ProgramSpider(scrapy.Spider):
    name = "program"
    allowed_domains = ["prathwik.fun"]
    start_urls = ["http://prathwik.fun/"]
    
    def request(self):
        url = 'https://prathwik.fun'
        return scrapy.Request(url = url, callback = self.parse)
				
    def parse(self, response):
        url = response.url
        title = response.css('h1::text').extract_first()
        print('Title is: {}'.format(title))