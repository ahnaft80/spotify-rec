from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    db = client["A4dbNorm"]

    recordings_collection = db["recordings"]

    result = recordings_collection.aggregate([
        { "$match": {
            "recording_id": { "$regex": "^70" } } }, 
        { "$group": {"_id": "", "recording_id": {"$first": "$recording_id"},
                      "avg_rhythmicality": {"$avg": "$rhythmicality"}} },
    ])
    with open('output.txt', 'w', encoding="utf-8") as f:
        for writer in result:
            f.write(str(writer) + '\n')