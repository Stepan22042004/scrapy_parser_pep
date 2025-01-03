import os
import csv
import datetime as dt

from collections import defaultdict

from pep_parse.settings import DATETIME_FORMAT, BASE_DIR, RESULT_FOLDER


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_count = defaultdict(int)
        if not os.path.exists(BASE_DIR / RESULT_FOLDER):
            os.makedirs(BASE_DIR / RESULT_FOLDER)

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / RESULT_FOLDER
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary__{now_formatted}.csv'
        file_path = results_dir / file_name
        status_list = tuple(self.status_count.items())

        total_count = sum(self.status_count.values())

        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            f.write('Статус,Количество\n')
            writer.writerows(status_list)
            f.write(f'Total,{total_count}\n')
