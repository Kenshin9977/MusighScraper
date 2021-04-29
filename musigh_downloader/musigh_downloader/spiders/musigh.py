import scrapy

from musigh_downloader.items import MusighFileItem
# from musigh_downloader.musigh_downloader.items import MusighFileItem


class MusighSpider(scrapy.Spider):
    name = 'musigh'
    start_urls = ['http://musigh.com/wp-content/uploads/']

    def parse(self, response):
        for i in range(4, response.xpath('//tr').__len__()):
            yield scrapy.Request(
                response.urljoin(response.xpath('//tr[' + str(i) + ']/td[2]/a').attrib['href']),
                self.parse_month
            )

    def parse_month(self, response):
        for i in range(4, response.xpath('//tr').__len__()):
            yield scrapy.Request(
                response.urljoin(response.xpath('//tr[' + str(i) + ']/td[2]/a').attrib['href']),
                self.scrap
            )

    def scrap(self, response):
        for i in range(4, response.xpath('//tr').__len__()):
            file_url = response.urljoin(response.xpath('//tr[' + str(i) + ']/td[2]/a').attrib['href'])
            yield MusighFileItem(file_urls=[file_url])



