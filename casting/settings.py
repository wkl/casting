# Scrapy settings for casting project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'casting'

SPIDER_MODULES = ['casting.spiders']
NEWSPIDER_MODULE = 'casting.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.71 Safari/537.36'

#DOWNLOAD_DELAY = 0.1  # 100 ms
#RANDOMIZE_DOWNLOAD_DELAY = True
DOWNLOAD_TIMEOUT = 20

# BFS order
# http://doc.scrapy.org/en/0.16/faq.html#does-scrapy-crawl-in-breadth-first-or-depth-first-order
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'
