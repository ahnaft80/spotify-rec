from pymongo import MongoClient
import sys


def main(argv):    
    # get port from argument and connect to server
    serverport = argv[0]
    client = MongoClient("mongodb://localhost:" + serverport)

    # use recordings collection from normalized db, other collection will not be required
    db = client["A4dbNorm"]
    recordings_collection = db["recordings"]

    # filter to only recordings whose recording id begins with 70
    # calculate average for the remaining group
    result = recordings_collection.aggregate([
        { "$match": {
            "recording_id": { "$regex": "^70" } } }, 

        { "$group": 
            {
            "_id": "",
            "avg_rhythmicality": {"$avg": "$rhythmicality"}
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