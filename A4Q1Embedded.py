from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    db = client["A4dbEmbedded"]

    collection = db["SongwritersRecordings"]

    result = collection.aggregate([
        { "$group": {"_id": "$_id", "songwriter_id": {"$first": "$songwriter_id"},
                      "name":{"$first": "$name"},
                        "num_recordings": { "$sum": { "$size": "$recordings" } } } },
    ])
    for writer in result:
        print(writer)