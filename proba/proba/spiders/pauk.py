from scrapy.shell import Shell
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.commands.shell import Command
import os

KLJUCNE_RECI = ["student", "studenti","blokada", "blokade" ,"incident", "referendum", "krv", "protest", "glumci", "mladi", "11:52", "zahtev", "štrajk", "sindikat", "prosveta", "fakultet"]
linkovi = set()

class CrawlingSpider(CrawlSpider):
    name = 'pauk'
    l = ""
    allowed_domains = ['n1info.rs', 'informer.rs', "rts.rs"]
    start_urls = ['http://n1info.rs/', 'http://informer.rs/', "https://www.rts.rs/" ]
    rules = [
        Rule(LinkExtractor(allow='/vesti', deny=["/?comments"]), callback='parse'),
        Rule(LinkExtractor(allow='/politika'), callback='parse'),

    ]


    def parse(self, response):
        for rec in KLJUCNE_RECI:
            if rec in response.url.lower() and "?comments" not in response.url.lower() :
                l = response.url.replace("HtmlResponse 200", "")
                yield {
                    "link" : response.url.replace("HtmlResponse 200", "")
                }



