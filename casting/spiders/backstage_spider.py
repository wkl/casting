from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from casting.items import CastingItem
from scrapy.http.request import Request
from scrapy import log
from urlparse import urljoin

class BackstageSpider(BaseSpider):
    name = "backstage"
    allowed_domains = ["backstage.com"]
    start_urls = [
        "http://www.backstage.com/casting/?min_age=1&max_age=120&union_status=&location=&geo=&radius=300&q=&sort_by=newest&page=1",
    ]
    base_url = "http://www.backstage.com"
    page_base_url = "http://www.backstage.com/casting/?min_age=1&max_age=120&union_status=&location=&geo=&radius=300&q=&sort_by=newest&page="

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        total_page = hxs.select('//div[@class="pagination"]/ul/li[@class="last"]/a/@data-page').extract()[0]

        page_requests = []
        for page in xrange(1, int(total_page) + 1):
        #for page in xrange(1, 3):
            page_url = self.page_base_url + str(page)
            yield Request(page_url, callback=self.parse_list)

    def parse_list(self, response):
        hxs = HtmlXPathSelector(response)
        castings = hxs.select('//a[@class="title callLink"]')
        detail_requests = []
        for casting in castings:
            detail_url = urljoin(self.base_url, casting.select('@href').extract()[0])
            request = Request(detail_url, callback=self.parse_detail)
            detail_requests.append(request)

        return detail_requests

    def parse_detail(self, response):
        hxs = HtmlXPathSelector(response)
        casting = hxs.select('//div[@id="main"]')
        item = CastingItem()
        item['title'] = casting.select('//h1[1]/text()').extract()[0]
        item['link'] = response.url

        return item
