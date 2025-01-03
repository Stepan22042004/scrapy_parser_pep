from collections import defaultdict
import csv
import datetime as dt
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary__{now_formatted}.csv'
        file_path = results_dir / file_name
        status_list = [['Статус', 'Количество']]
        status_list.extend(self.status_count.items())
        total_count = sum(self.status_count.values())
        status_list.append(['Total', total_count])
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            for row in (self.status_count.keys(), self.status_count.values()):
                writer.writerows(status_list)
