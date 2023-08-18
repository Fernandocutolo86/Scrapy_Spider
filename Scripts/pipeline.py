import csv
import os

class QuotesPipeline:
    def open_spider(self, spider):
        self.csv_file = open('quotes.csv', 'w', encoding='utf-8-sig', newline='')
        self.csv_writer = csv.writer(self.csv_file, delimiter=';')
        self.csv_writer.writerow(['author', 'tags', 'page_number', 'rule_number', 'txt_filename'])

    def close_spider(self, spider):
        self.csv_file.close()

    def process_item(self, item, spider):
        txt_filename = f'quote_{item["rule_number"]}_{item["author"]}.txt'
        with open(txt_filename, 'w', encoding='utf-8') as txt_file:
            txt_file.write(item['text'])

        self.csv_writer.writerow([item['author'], ', '.join(item['tags']), spider.page_number, item['rule_number'], txt_filename])
        return item





