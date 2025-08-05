import scrapy


class LightnewparsSpider(scrapy.Spider):
    name = "lightnewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://divan.ru/category/svet"]

    def parse(self, response):
        lums = response.css('div.WdR1o')
        # Настраиваем работу с каждым отдельным светильником в списке
        for lum in lums:
            yield {

                'name': lum.css('div.lsooF span::text').get(),
                'price': lum.css('div.pY3d2 span::text').get(),
                'url': lum.css('a').attrib['href']
            }

            # Находим ссылку на следующую страницу
        next_page = response.css('a.PaginationLink ui-xZAsN__next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)