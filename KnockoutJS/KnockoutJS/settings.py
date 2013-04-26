# Scrapy settings for KnockoutJS project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'Dash Documenter for KnockoutJS'

SPIDER_MODULES = ['KnockoutJS.spiders']
NEWSPIDER_MODULE = 'KnockoutJS.spiders'
ITEM_PIPELINES = ['KnockoutJS.pipelines.KnockoutjsPipeline']
DOCSET_PATH = "/Users/dom/Dropbox/dev/DashDocumenter/KnockoutJS.docset"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'KnockoutJS (+http://www.yourdomain.com)'
