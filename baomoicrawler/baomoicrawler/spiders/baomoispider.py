# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from baomoicrawler.items import BaomoicrawlerItem
from scrapy.exceptions import CloseSpider

class BaomoispiderSpider(CrawlSpider):
    name = 'baomoispider'
    allowed_domains = ['baomoi.com']
    start_urls = ['baomoi.com']
    with open("/home/vudat1710/Downloads/Training OSP/Training week 1-2/Fresher_Data_Science_week1-2/Week 1/Crawler/baomoicrawler/link_week5.txt", "r") as f:
        for line in f.readlines():
            start_urls.append(line.strip())
    f.close()
    print(start_urls)

    MAX = 5000
    count = 0
    rules = (Rule(LinkExtractor(restrict_xpaths=('//*[@class="control__next"]'), deny=('\S+/c/\S+','\S+/t/\S+', '\S+/trang\d{3,}.epi', '\S+/trang([4-9]\d|\d{3,}).epi')),callback="parse_items",follow= True),)
    
    def parse_items(self, response):
        urls = response.xpath('//*[@class="cache"]/@href')
        for url in urls:
            connect_to_url = response.urljoin(url.extract())
            yield Request(connect_to_url, callback=self.parse_question)

    def parse_question(self, response):
        item = BaomoicrawlerItem()
        # item['title'] = response.xpath('//*[@class="article__header"]/text()').extract_first().strip()
        # item['time'] = response.xpath('//*[@class="time"]/text()').extract_first().strip()
        # item['summary'] = response.xpath('//*[@class="article__sapo"]/text()').extract_first().strip()
        contents = response.xpath('//*[@class="body-text"]/text()').extract()
        contents = [content.strip() for content in contents]
        item['content'] = " ".join(contents)
        # tags = response.xpath('//*[@class="keyword"]/text()').extract()
        # tags = [tag.strip()for tag in tags]
        # item['tags'] = ", ".join(tags) 
        # item['link'] = response.request.url 
        item['topic'] = response.xpath('//*[@class="cate"]/text()').extract_first().strip()       
        # source = response.xpath('//*[@class="article__meta"]/a[@class="source"]/text()').extract()
        # source = [s.strip() for s in source]
        # source = "".join(source)
        # source_link = response.xpath('//*[@class="sourceLink"]/@href').extract_first()
        # full_source_link = response.urljoin(source_link)
        # item['source'] = (source + ': ' + full_source_link)
        self.count += 1
        if self.count > self.MAX:
            raise CloseSpider('20000 pages crawled')

        yield item
