# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SouqcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Title			=	scrapy.Field()
    Category		=	scrapy.Field()
    OriginalPrice	=	scrapy.Field()
    CurrentPrice	=	scrapy.Field()
    Discounted		=	scrapy.Field()
    Savings			=	scrapy.Field()
    SoldBy			=	scrapy.Field()
    SellerRating	=	scrapy.Field()
    Url				=	scrapy.Field()
    pass
