import scrapy
import csv
import os


class NepalicalenderSpider(scrapy.Spider):
    name = "nepalicalender"
    allowed_domains = ["nepalicalendar.rat32.com"]
    start_urls = ["https://nepalicalendar.rat32.com"]

    def parse(self, response):
        vegetable_link = response.xpath('//a[@title="kalimati Vegetable Rates"]')
        sub_url = vegetable_link.xpath('@href').get()
        yield response.follow(sub_url, callback=self.parse_vegetable_price, meta={'name': vegetable_link})


    def parse_vegetable_price(self, response):
        date = response.xpath(
            '//*[@id="vtitle"]/text()').extract_first().split('-')[-1].strip()
        title = response.xpath('//*[@id="vtitle"]/text()').extract_first()
        table_headers = [element.split(" ")[0] for element in response.xpath(
            '//*[@id="commodityDailyPrice"]/thead/tr/th/text()').extract()] + ["Date"]
        vegetables_data = response.xpath(
            '//*[@id="commodityDailyPrice"]/tbody/tr/td/text()').extract()
        vegetables_names = vegetables_data[::5]
        units = vegetables_data[1::5]
        minimum_price = vegetables_data[2::5]
        maximum_price = vegetables_data[3::5]
        average_price = vegetables_data[4::5]

        # Sample scraped data (dictionary format)
        scraped_data = {
            'Title': title,
            'Date': date,
            'table_headers': table_headers,
            'vegetables_names': vegetables_names,
            'units': units,
            'minimum_price': minimum_price,
            'maximum_price': maximum_price,
            'average': average_price,
        }

        yield scraped_data


