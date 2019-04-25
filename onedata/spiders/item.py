import scrapy

class itemer(scrapy.Spider):
    name = 'items'
    start_urls = ['http://lab.scrapyd.cn']

    def parse(self,response):
        paqu1 = response.css('div.quote')[1]

        text = paqu1.css('.text::text').extract_first()
        autor = paqu1.css('.author::text').extract_first()
        tags = paqu1.css('.tags .tag::text').extract()
        tags = ",".join(tags)

        filename = '%s-语录.txt' %autor
        f = open(filename,"a+",encoding='utf-8')
        f.write(text)
        f.write('\n')
        f.write('标签: '+tags)
        f.close()