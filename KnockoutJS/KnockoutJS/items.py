# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

# We actually don't need this
class BindingItem(Item):
    title = Field()
    path = Field()
