from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    db = client["A4dbEmbedded"]

    collection = db["SongwritersRecordings"]
    
    result = collection.aggregate([
        { "$unwind": "$recordings"},
        { "$match": {
            "recordings.recording_id": { "$regex": "^70" } } }, 
        { "$group": {"_id": "", "recording_id": {"$first": "$recordings.recording_id"},
                      "avg_rhythmicality": {"$avg": "$recordings.rhythmicality"}} },
    ])
    with open('output.txt', 'w', encoding="utf-8") as f:
        for writer in result:
            f.write(str(writer) + '\n')