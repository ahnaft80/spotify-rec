from pymongo import MongoClient
import sys

def main(argv):
    # get port from argument and connect to server
    serverport = argv[0]
    client = MongoClient("mongodb://localhost:" + serverport)
    # use embedded db
    db = client["A4dbEmbedded"]
    collection = db["SongwritersRecordings"]

    # unwind the recordings so that each songwriter is associated with just 1
    # group items by songwriter id summing all recording length fields, set object id to be songwriter id
    # filter to only songwriters with total length greater than 0
    result = collection.aggregate([
        { "$unwind": "$recordings"},
        { "$group": 
            {
            "_id": "$songwriter_id",
            "total_length": { "$sum": "$recordings.length" },
            "songwriter_id": {"$first": "$songwriter_id"},
            } 
        },
        {"$match":
            {
                "total_length":{"$gt":0}
            }
        }

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