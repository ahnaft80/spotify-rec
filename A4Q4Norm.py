from pymongo import MongoClient
from datetime import datetime
import sys


def main(argv):    
    # get port from argument and connect to server
    serverport = argv[0]
    client = MongoClient("mongodb://localhost:" + serverport)

    # use recordings collection from normalized db, other collection will be accessed via lookup
    db = client["A4dbNorm"]
    recordings_collection = db["recordings"]

    # get date to compare to
    date = datetime(1950, 1, 1)

    # get all recordings which are not before 1950
    # match them with the appropriate songwriter
    # filter to only songwriter name, recording name, and recording issue date fields
    # unwind songwriter name so it does not appear as a list (songs with multiple songwriters will appear twice)
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