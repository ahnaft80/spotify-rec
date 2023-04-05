from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime



if __name__ == "__main__":
    client = MongoClient()
    db = client["A4dbNorm"]

    recordings_collection = db["recordings"]

    date = datetime(1950, 1, 1)

    result = recordings_collection.aggregate([
        {"$match":
            {
                "issue_date":{"$gte":date}
            }
        },
        {"$lookup":
            {
                "localField":"songwriter_ids",
                "from":"songwriters",
                "foreignField":"songwriter_id",
                "as":"songwriters"
            }
        },
        {"$project":
            {
                "name":"$songwriters.name",
                "r_name":"$name",
                "r_issue_date":"$issue_date",                
            }
        },
        {"$unwind":"$name"}
    ])

    with open('output.txt', 'w', encoding="utf-8") as f:
        for writer in result:
            f.write(str(writer) + '\n')