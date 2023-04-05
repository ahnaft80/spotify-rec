from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    db = client["A4dbNorm"]

    songwriters_collection = db["songwriters"]

    # match each songwriter with their recordings 
    # unwind the recordings so that each songwriter is associated with just 1
    # group by items by songwriter id summing all recording length fields, do id by songwriter id
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
            {"_id": "$songwriter_id", "total_length": { "$sum": "$recordings.length" }, "songwriter_id": {"$first": "$songwriter_id"},
             } 
        },


    ])

    with open('output.txt', 'w', encoding="utf-8") as f:
        for writer in result:
            f.write(str(writer) + '\n')