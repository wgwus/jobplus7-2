import scrapy


class JobSpider(scrapy.Spider):
    name = 'company'

    start_urls = ['https://www.lagou.com/gongsi/']
    def parse(self,response):
        for company in response.css('li.company-item'):
            yield {
               # 'companyname':job.xpath('//div[@class"company-name"]/h2')
               'logo':company.xpath('.//div[@class="top"]/p/a/img/@src').extract_first(),
               'username':company.xpath('.//div[@class="top"]/p/a/text()').extract_first(),
               'description':company.xpath('.//div[@class="top"]/p[4]/text()').extract_first(),
               'about':company.xpath('.//div[@class="top"]/p[5]/text()').extract_first()
            }
        '''
        for job in response.xpath('//div[@class="company-list"]/a/@href'):
            yield response.follow(url,callback=self.parse)
            '''

        #for job in response.xpath('//div[@class="top"]').extract()
