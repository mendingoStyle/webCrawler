import scrapy
from scrapy.http.request import Request


class SmartphoneSpider(scrapy.Spider):
    name = "smartphone_spider"
    
    def start_requests(self):

        headers = {
            "Host": "www.casasbahia.com.br",
            "Connection": "keep-alive",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "DNT": "1",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language":"pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6",
        }

        yield Request(url= 'https://www.casasbahia.com.br/c/telefones-e-celulares/smartphones/?Filtro=c38_c326&nid=201546', callback=self.parse, headers=headers)

    def parse(self, response):

        jsonList = []

        breadcrumb2 = ''
        breadcrumb3 = ''
        BREADCRUMB_SELECTOR = '.breadcrumb'
        for brickset in response.css(BREADCRUMB_SELECTOR):

            CAT2_SELECTOR = './ol/li[2]/a/span/text()'
            CAT3_SELECTOR = './ol/li[3]/span/text()'

            breadcrumb2 = brickset.xpath(CAT2_SELECTOR).extract_first()
            breadcrumb3 = brickset.xpath(CAT3_SELECTOR).extract_first()

        CONTAINER_SELECTOR = '.cont-product'
        for brickset in response.css(CONTAINER_SELECTOR):
        
            CODE_SELECTOR = './a/div/@id'
            NAME_SELECTOR = 'span ::text'
            PRICE_SELECTOR = './a/div/span/span/strong/text()'


            yield {
                'category': breadcrumb2 + "/" + breadcrumb3,
                'code': brickset.xpath(CODE_SELECTOR).extract_first(),
                'name': brickset.css(NAME_SELECTOR).extract_first(),
                'price': brickset.xpath(PRICE_SELECTOR).extract_first()
            }
