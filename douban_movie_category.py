# -*- coding: utf-8 -*-
#!/usr/bin/env python

from scrapy.spider import Spider
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
#from douban_movie_category.items import DoubanMovieCategoryItem
import jieba

class CategorySpider(Spider):
	name = "category_spider"
	allowed_domains = ["www.movie.douban.com"]
	start_urls = [
		'http://movie.douban.com/top250?start=225&filter=&type=',
	]
	
	def parse(self,response):
		sel = Selector(response)
		item = DoubanMovieCategoryItem()
		category = sel.xpath("//div[@class='info']/div[@class='bd']/p/text()").extract()
		
		print type(category)
		x = []
		for i in category:
			if len(i)>5 and ':' not in i:
				i = i.split('/')
				i = i[len(i)-1]
				
				i = i.strip()
				i = i.replace(" ","")
				word = unicode(i)
				
				if word != " " and len(word)>0:
					print len(word)
					print word
					
					words = jieba.cut(word,cut_all = False)
					for n in words:
						print n
						x.append(n)
		
		item['categories'] = x
		yield item
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		