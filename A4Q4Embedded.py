from pymongo import MongoClient
from datetime import datetime


if __name__ == "__main__":
    client = MongoClient()
    db = client["A4dbEmbedded"]

    # get date to compare to
    date = datetime(1950, 1, 1)


    # unwind on recordings so that each songwriter object has just 1 recording
    # reduce the collection to just songwriter name, recording name, and recording issue date
    # filter out entries with an issue date before 1950
    
    collection = db["SongwritersRecordings"]
    result = collection.aggregate([
        {"$unwind":"$recordings"},
        {"$project":
            {
                "name":1,
                "r_name":"$recordings.name",
                "r_issue_date":"$recordings.issue_date"
            }
        },
        {"$match":
            {
                "r_issue_date":{"$gte":date}
            }
        }
    ])

    with open('output.txt', 'w', encoding="utf-8") as f:
        for writer in result:
            f.write(str(writer) + '\n')