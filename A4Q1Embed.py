from pymongo import MongoClient
import sys

def main(argv):
    # get port from argument and connect to server
    serverport = argv[0]
    client = MongoClient("mongodb://localhost:" + serverport)
    # use embedded db
    db = client["A4dbEmbedded"]
    collection = db["SongwritersRecordings"]


    # group all songwriters by id and sum the number of their recordings
    # filter to only those with 1 or more recording
    result = collection.aggregate([
        { "$group": 
            {   "_id": "$_id",
                "songwriter_id": {"$first": "$songwriter_id"},
                "name":{"$first": "$name"},
                "num_recordings": { "$sum": { "$size": "$recordings" } } 
            } 
        },
        {"$match":
            {
                "num_recordings":{"$gte":1}
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