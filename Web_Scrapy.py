import scrapy


class WebScrapy(scrapy.Spider):
    name = "WS"

    def __init__(self, *args, **kwargs):
        super(WebScrapy, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('start_urls')]

    def parse(self, response, **kwargs):
        quotes = response.xpath("*//ul[@class='statistics']/li")
        for q in quotes:
            yield {
                'title': q.xpath(".//span[not(@class)]//text()[2]").get(),
                'value': (q.xpath(".//div[@class='main-info']/strong/text()").get()).replace('\n', ''),
            }
