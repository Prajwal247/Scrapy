import pymongo

class MongoDBPipeline:
    collection_name = 'prices'  # Replace with your desired collection name
    db_name = 'vegetable_prices'  # Replace with your desired database name

    def __init__(self):
        self.mongo_uri = 'mongodb+srv://prazzwalthapa87:Ohmygod123@cluster0.1fwe1vz.mongodb.net'
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.db_name]  # Access the desired database
        self.collection = self.db[self.collection_name]  # Access the desired collection

    def process_item(self, item, spider):
        try:
            self.collection.insert_one(dict(item))
        except Exception as e:
            self.logger.error(f"Error processing item: {e}")
        return item
