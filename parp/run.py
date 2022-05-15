from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from parp.spiders.uslugirozwojowe import UslugirozwojoweSpider


if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())
    process.crawl(UslugirozwojoweSpider)
    process.start()
