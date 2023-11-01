import pymongo

# Define your MongoDB Atlas connection string
mongo_uri = (
    "mongodb+srv://prazzwalthapa87:Ohmygod123@your-cluster.mongodb.net/vegetable_prices"
)

# Create a MongoClient instance with the connection string
client = pymongo.MongoClient(mongo_uri)

# Access the specific database you want to work with
db = client["vegetable_prices"]

# Access a collection within the database
collection = db["prices"]
