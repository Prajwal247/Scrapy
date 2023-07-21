import scrapy
import csv
import os


class NepalicalenderSpider(scrapy.Spider):
    name = "nepalicalender"
    allowed_domains = ["nepalicalendar.rat32.com"]
    start_urls = ["https://nepalicalendar.rat32.com/vegetable"]

    def parse(self, response):
        date = response.xpath('//*[@id="vtitle"]/text()').extract_first().split('-')[-1].strip()
        title = response.xpath('//*[@id="vtitle"]/text()').extract_first()
        table_headers = [element.split(" ")[0] for element in response.xpath('//*[@id="commodityDailyPrice"]/thead/tr/th/text()').extract()] + ["Date"]
        vegetables_data =  response.xpath('//*[@id="commodityDailyPrice"]/tbody/tr/td/text()').extract()
        vegetables_names = vegetables_data[::5]
        units =  vegetables_data[1::5]
        minimum_price =  vegetables_data[2::5]
        maximum_price =  vegetables_data[3::5]
        average_price =  vegetables_data[4::5]

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

        # Extract the table headers and rows
        table_headers = scraped_data['table_headers']
        rows = list(zip(scraped_data['vegetables_names'], scraped_data['units'], scraped_data['minimum_price'], scraped_data['maximum_price'], scraped_data['average'],[scraped_data['Date']] * len(scraped_data['vegetables_names'])))

        # Define the file name for the CSV file
        file_name = 'vegetables_price.csv'

        # Check if the file exists
        if os.path.exists(file_name):
            # Read the last row's date from the existing CSV file
            with open(file_name, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                last_row = None
                for row in csv_reader:
                    last_row = row
                last_row_date = last_row[-1] if last_row else None

            # Check if the last row's date is not equal to the current date
            if last_row_date != scraped_data['Date']:
                # File exists, and the date is different, so we'll append the new data
                with open(file_name, 'a', newline='') as csvfile:
                    csv_writer = csv.writer(csvfile)
                    csv_writer.writerows(rows)  # Append the new rows
        else:
            # File doesn't exist, so we'll create a new file and write the data
            with open(file_name, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(table_headers)  # Write the headers
                csv_writer.writerows(rows)  # Write the rows

        print(f"Scraped data has been updated and saved to {file_name}.")

