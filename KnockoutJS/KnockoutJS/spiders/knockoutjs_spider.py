from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from bs4 import BeautifulSoup
from KnockoutJS.items import BindingItem
import sqlite3 as lite
from KnockoutJS.settings import DOCSET_PATH


class KnockoutJSSpider(BaseSpider):
    name = "knockoutjs"
    allowed_domains = ["knockoutjs.com"]
    start_urls = [
        "http://knockoutjs.com/documentation/introduction.html",
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        con = lite.connect(DOCSET_PATH + '/Contents/Resources/docSet.dsidx')
        with con:

            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS searchIndex")
            cur.execute("CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT)")

            items = []
            for a in hxs.select("//ol/li/a[@href[contains(., '.html')]]"):

                soup = BeautifulSoup(a.extract())
                path = soup.a['href']
                path = path[len('../'):]

                if path.endswith('-binding.html'):
                    type = "Binding"
                    try:
                        title = soup.code.get_text()
                    except Exception:
                        title = soup.get_text()
                else:
                    type = "Guide"
                    title = soup.get_text()

                cur.execute("INSERT INTO searchIndex(name, type, path) VALUES(?, ?, ?)", (title, type, path))
                # item = BindingItem()
                # item['title'] = title
                # item['path'] = path
                # items.append(item)

        return items

