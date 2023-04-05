from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    db = client["A4dbEmbedded"]

    collection = db["SongwritersRecordings"]
    result = collection.aggregate([
        { "$unwind": "$recordings"},
        { "$group": {"_id": "$songwriter_id", "total_length": { "$sum": "$recordings.length" }, "songwriter_id": {"$first": "$songwriter_id"},
                         } },
    ])
    with open('output.txt', 'w', encoding="utf-8") as f:
        for writer in result:
            f.write(str(writer) + '\n')