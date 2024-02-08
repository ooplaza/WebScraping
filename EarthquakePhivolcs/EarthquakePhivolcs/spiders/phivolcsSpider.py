import scrapy


class PhivolcsspiderSpider(scrapy.Spider):
    name = "phivolcsSpider"
    allowed_domains = ["earthquake.phivolcs.dost.gov.ph"]
    start_urls = ["https://earthquake.phivolcs.dost.gov.ph/"]

    def parse(self, response):
        pass
