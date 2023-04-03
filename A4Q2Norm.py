from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    db = client["A4dbNorm"]

    songwriters_collection = db["recordings"]

    result = songwriters_collection.aggregate([
        { "$match": {
            "recording_id": { "$regex": "^70" } } }, 
        { "$group": {"_id": "", "recording_id": {"$first": "$recording_id"},
                      "avg_rhythmicality": {"$avg": "$rhythmicality"}} },
    ])
    for writer in result:
        print(writer)