# -*- coding: utf-8 -*-
import scrapy

class GetlinkSpider(scrapy.Spider):
    name = 'getlink'
    allowed_domains = ['baomoi.com']
    start_urls = ['http://baomoi.com/']

    def parse(self, response):
        links = response.xpath('//*[@class="l-grid"]/ul/li/a/@href').extract()
        links = [response.urljoin(link) for link in links if "epi" in link]
        with open("link.txt", "a") as f:
            for link in links:
                f.write(link)
                f.write("\n")
        f.close()

