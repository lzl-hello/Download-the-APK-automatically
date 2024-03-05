import scrapy

from ScrapyAPK.items import ScrapyapkItem

class ZhushouSpider(scrapy.Spider):
    name = "zhushou"
    allowed_domains = ["apkpure.com"]

    # start_urls = ["https://apkpure.com/cn/tools"]

    def start_requests(self):
        base_url = "https://apkpure.com/cn/tools?page={}"
        total_pages = 3  # 假设要获取前3页的数据
        for page in range(1, total_pages + 1):
            url = base_url.format(page)
            yield scrapy.Request(url=url, callback=self.parse)
    # start_urls = ["https://apkpure.com/cn/tools?page=1"]

    def parse(self, response):

        # 获取所有的li元素
        li_elements = response.xpath('/html/body/main/div[5]/div[2]/div[1]/div/div/ul/li')
        for li in li_elements:
            item = ScrapyapkItem()
            # 提取name属性值
            name = li.xpath('.//a[contains(@class, "grid-item-title")]/text()').get()
            if name:
                print("应用名称：" + name)
                item['name'] = name
            # 提取version属性值
            version = li.xpath('.//div[contains(@class, "grid-row")]/@data-dt-version').get()
            if version:
                print("版本号：" + version)
                item['version'] = version
            # 提取一级页面的下载链接
            download_element = li.xpath(
                './/a[contains(@class, "apk-grid-download") and contains(@class, "apk-grid-button")]')
            # 提取href属性值
            href = download_element.xpath('./@href').get()
            if href:
                # 构造请求，继续请求下载链接
                # yield scrapy.Request(url=href, callback=self.parse_download_page)
                yield scrapy.Request(url=href, callback=self.parse_download_page, meta={'item': item})

        yield item


    def parse_download_page(self, response):


        # download_link = response.xpath('/html/body/div[3]/main/div[4]/a[1]/@href').get()
        download_link = response.xpath(
            '//a[contains(@class, "btn") and contains(@class, "download-start-btn")]/@href').get()
        if download_link:
            print("下载链接：" + download_link)
            # item = ScrapyapkItem()
            # item['url'] = download_link
            # yield item
            item = response.meta['item']
            item['url'] = download_link
            yield item
        else:
            print("未获取到下载链接")




