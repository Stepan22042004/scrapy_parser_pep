from collections import defaultdict
import csv
import datetime as dt

from pep_parse.settings import BASE_DIR, DATETIME_FORMAT, RESULT_FOLDER


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary__{now_formatted}.csv'
        file_path = BASE_DIR / RESULT_FOLDER / file_name
        total_count = sum(self.status_count.values())
        status_list = (('Статус', 'Количество'),)
        status_list += tuple(self.status_count.items())
        status_list += (('Total', total_count),)

        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(status_list)
