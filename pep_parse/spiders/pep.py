import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        urls = response.css('a[href^="pep"]')
        for url in urls:
            yield response.follow(url, callback=self.parse_pep)

    def parse_pep(self, response):
        info = response.css('title::text').get().split(' ')
        lst = response.css('title::text').get().split(' – ')[1]
        number = info[1]
        name = lst[:len(lst) - len(' | peps.python.org'):]

        data = {
            'name': name,
            'number': number,
            'status': response.css('abbr::text').get()
        }
        yield PepParseItem(data)
