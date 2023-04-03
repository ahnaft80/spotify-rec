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
    with open('output.txt', 'w', encoding="utf-8") as f:
        for writer in result:
            f.write(str(writer) + '\n')