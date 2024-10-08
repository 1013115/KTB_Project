import scrapy

class NewsbotSpider(scrapy.Spider):
    name = "newsbot"
    allowed_domains = ["news.naver.com"]
    start_urls = ["https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=100"]

    def parse(self, response):
        titles = response.xpath('//ul[@class="type06_headline"]/li/dl/dt[2]/a/text()').extract()
        authors = response.css('.writing::text').extract()
        previews = response.css('.lede::text').extract()
        
        for item in zip(titles, authors, previews):
            scraped_info = {
                'title': item[0].strip(),
                'author': item[1].strip(),
                'preview': item[2].strip(),
            }
            yield scraped_info
