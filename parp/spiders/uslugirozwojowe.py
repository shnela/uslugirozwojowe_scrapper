import scrapy
from scrapy.spiders import Spider


class UslugirozwojoweSpider(Spider):
    name = 'uslugirozwojowe'
    allowed_domains = ['uslugirozwojowe.parp.gov.pl']
    start_urls = [
        'https://uslugirozwojowe.parp.gov.pl/wyszukiwarka/uslugi/szukaj'
        '?nazwaUslugi=&identyfikatorProjektu=&identyfikatorProjektu%5B%5D=166&rodzaj='
        '&rodzaj%5B%5D=145&formaSwiadczenia=&kkz=0&kkzLista=&kuz=0&kuzLista='
        '&nabycieKwalifikacji=0&kategoria=&kategoria%5B%5D=479&dataRozpoczeciaUslugi='
        '&dataZakonczeniaUslugi=&ocena=0%2C5&cenaZaGodzine=0&cenaBruttoZaUslugeOd='
        '&cenaBruttoZaUslugeDo=&cenaBruttoOd=&cenaBruttoDo=&mozliwoscDofinansowania=0'
        '&mozliwoscDofinansowania=1&miejsceSzkolenia=&miejscowoscId=&promienZasiegu=100'
        '&dostawcyUslug=&per-page=10&order=score',
    ]

    def parse(self, response, **kwargs):
        course_vendor_urls = response.xpath("//p[contains(@class, 'service-name')]//a/@href").extract()
        for vendor_url in course_vendor_urls:
            absolute_vendor_url = response.urljoin(vendor_url)
            yield scrapy.Request(
                url=absolute_vendor_url,
                callback=self.parse_vendor,
            )

    def parse_vendor(self, response, **kwargs):
        vendor_name = response.xpath("//p[contains(@class, 'service-provider-name')]/text()").extract_first()
        yield {"name": vendor_name}
