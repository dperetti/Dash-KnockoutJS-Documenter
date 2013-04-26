# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting


#https://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
from KnockoutJS.items import BindingItem


# We actually don't need this
class KnockoutjsPipeline(object):
    def process_item(self, item, spider):
        #print type(item) is BindingItem
        return item
