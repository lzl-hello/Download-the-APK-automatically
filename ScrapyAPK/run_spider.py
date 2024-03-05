from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging
from ScrapyAPK.spiders.zhushou import ZhushouSpider
import threading

def run_spider():
    process = CrawlerProcess(get_project_settings())
    process.crawl(ZhushouSpider)
    process.start()

# 设置日志
configure_logging()

# 定义线程列表
threads = []


# 在主线程中启动爬虫
run_spider()



# 多线程咋改？？
# # 启动多个线程
# for i in range(5):  # 假设要启动5个线程
#     thread = threading.Thread(target=run_spider)
#     threads.append(thread)
#     thread.start()
#
# # 等待所有线程完成
# for thread in threads:
#     thread.join()
