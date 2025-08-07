import scrapy

class ShopifyLeadSpider(scrapy.Spider):
    name = 'shopify_leads'
    custom_settings = {'ROBOTSTXT_OBEY': True}
    start_urls = [line.strip() for line in open('seed_shopify_domains.txt')]

    def parse(self, response):
        yield {
            'domain': response.url.split('/')[2],
            'shop_name': response.xpath('//title/text()').get(default='').strip(),
            'meta_desc': response.xpath('//meta[@name="description"]/@content').get(default='').strip(),
            'tech_recharge': 'recharge' in response.text.lower(),
        }

