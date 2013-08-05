# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class CastingItem(Item):
    title = Field()
    link = Field()
    start_date = Field()
    posted_date = Field()
    modified_date = Field()
