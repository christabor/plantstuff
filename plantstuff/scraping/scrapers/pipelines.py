# -*- coding: utf-8 -*-

import json
import os

import pymongo


class ScrapersPipeline(object):
    """Default scraper pipeline."""

    def process_item(self, item, spider):
        """Process single item."""
        return item


class JsonPipeline(object):
    """Customized json outputer pipeline."""

    def open_spider(self, spider):
        """Open buffer."""
        if hasattr(spider, 'category'):
            fname = '{}_{}'.format(spider.name, spider.category)
        else:
            fname = spider.name
        data_dir = spider.settings.get('PIPELINE_DATA_DIR')
        fpath = os.path.join(data_dir, fname)
        self.file = open('{}.json'.format(fpath), 'w')
        self.file.truncate(0)
        self._items = []

    def close_spider(self, spider):
        """Close file."""
        self.file.write(json.dumps(self._items, indent=2, sort_keys=True))
        self.file.write('\n')
        self.file.close()

    def process_item(self, item, spider):
        """Process single item."""
        filtered = {}
        for k, v in item.items():
            if v == '':
                filtered[k] = None
            else:
                filtered[k] = v.strip() if isinstance(v, str) else v
            if isinstance(v, list):
                v = [token for token in v if token]
        self._items.append(filtered)
        return filtered


class MongoPipeline(object):

    collection_name = 'plantstuff_raw'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'plants')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item
