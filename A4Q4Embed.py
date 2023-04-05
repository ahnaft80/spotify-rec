from pymongo import MongoClient
from datetime import datetime
import sys

def main(argv):
    # get port from argument and connect to server
    serverport = argv[0]
    client = MongoClient("mongodb://localhost:" + serverport)
    # use embedded db
    db = client["A4dbEmbedded"]
    collection = db["SongwritersRecordings"]

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
        },
        
    ])


    # print each item in the query result
    for item in result:
        print (item)


    # write to file for testing
    '''
    with open('output.txt', 'w', encoding="utf-8") as f:
        for writer in result:
            f.write(str(writer) + '\n')
    '''
    client.close()

if __name__ == "__main__":
    # call main with port argument
    main(sys.argv[1:])