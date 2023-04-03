from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    db = client["A4dbNorm"]

    songwriters_collection = db["songwriters"]

    result = songwriters_collection.aggregate([
        { "$group": {"_id": "$_id", "songwriter_id": {"$first": "$songwriter_id"},
                      "name":{"$first": "$name"},
                        "num_recordings": { "$sum": { "$size": "$recordings" } } } },
    ])
    for writer in result:
        print(writer)