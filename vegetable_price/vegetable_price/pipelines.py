from pymongo import MongoClient
from scrapy.settings import Settings

class MongoDBPipeline(object):

    def __init__(self):
        settings = Settings()
        connection = MongoClient(
            settings.get('MONGODB_SERVER'),
            settings.get('MONGODB_PORT')
        )
        db_name = str(settings.get('MONGODB_DB'))
        db = connection[db_name]

        self.collection = db[str(settings.get('MONGODB_COLLECTION'))]

    def process_item(self, item, spider):
        print(item)
        self.collection.insert(dict(item))
        return item
