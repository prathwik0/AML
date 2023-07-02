import scrapy


class ParagraphSpider(scrapy.Spider):
    name = "paragraph"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["http://wikipedia.org/"]

    def request(self):
        urls = [
            "https://en.wikipedia.org/wiki/Titanic",
            "https://en.wikipedia.org/wiki/Titanic_(1997_film)",
        ]
        return [scrapy.Request(url=url, callback=self.parse) for url in urls]

    def parse(self, response):
        url = response.url
        paras = response.css("h1::text").getall()
        print(paras)
        for para in paras:
            print("Paragraph : ", para)
