from pymongo import MongoClient
import sys

def main(argv):
    # get port from argument and connect to server
    serverport = argv[0]
    client = MongoClient("mongodb://localhost:" + serverport)
    # use embedded db
    db = client["A4dbEmbedded"]
    collection = db["SongwritersRecordings"]
    
    # unwind recordings to allow for filtering
    # filter to only recordings whose recording id begins with 70
    # calculate average for the remaining group
    result = collection.aggregate([
        { "$unwind": "$recordings"},
        { "$match": {
            "recordings.recording_id": { "$regex": "^70" } } },
         
        { "$group": 
            {"_id": "",
            "avg_rhythmicality": {"$avg": "$recordings.rhythmicality"}
            } },
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