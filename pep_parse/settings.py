from pathlib import Path


BASE_DIR = Path(__file__).parent.parent

RESULT_FOLDER = 'results'

BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = f'{BOT_NAME}.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]


ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

ROBOTSTXT_OBEY = True

FEEDS = {
    f'{RESULT_FOLDER}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
    },
}

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
