import csv
import datetime as dt
import os
from collections import defaultdict

from pep_parse.settings import BASE_DIR, DATETIME_FORMAT, RESULT_FOLDER


class PepParsePipeline:
    def __init__(self):
        os.makedirs(BASE_DIR / RESULT_FOLDER, exist_ok=True)

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
        status_list = (
            ('Статус', 'Количество'),
            *self.status_count.items(),
            ('Всего', sum(self.status_count.values())),
        )

        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(status_list)
