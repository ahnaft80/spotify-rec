from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    db = client["A4dbNorm"]

    songwriters_collection = db["songwriters"]
    recordings_collection = db["recordings"]


    result = songwriters_collection.aggregate([
        
        {"$lookup":{
            "localField":"recordings",
            "from":"recordings",
            "foreignField":"recording_id",
            "as":"recordings"
            }
        },
        {"$unwind": "$recordings"},
        { "$group": 
            {"_id": "$_id", "songwriter_id": {"$first": "$songwriter_id"},
            "total_length": { "$sum": "$recordings.length" } } 
        },


    ])

    with open('output.txt', 'w', encoding="utf-8") as f:
        for writer in result:
            f.write(str(writer) + '\n')