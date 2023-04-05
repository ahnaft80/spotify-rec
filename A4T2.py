from pymongo import MongoClient
import json
from bson.json_util import loads, dumps
import sys

def main(argv):
    # read in the json files
    with open('recordings.json', 'rb') as f1:
        recordings = json.load(f1)

    with open('songwriters.json', 'rb') as f2:
        songwriters = json.load(f2)

    # get port from argument and connect to server
    serverport = argv[0]
    client = MongoClient("mongodb://localhost:" + serverport)
    db = client["A4dbEmbedded"]

    # create SongwritersRecordings collection
    collection = db["SongwritersRecordings"]
    collection.delete_many({})  # delete all previous entries in the collection

    # create a temporary recordings collection to help create the main collection
    recordings_collection = db["recordings"]
    recordings_collection.delete_many({})
    for recording in recordings:
        recording = loads(dumps(recording))     # fix formatting
        ret_record = recordings_collection.insert_one(recording)

    ''' The loop does the following things: 
        1. For each songwriter, get the list of recording ids
        2. For each recording id, get the recording from the recordings collection
        3. Remove the songwriter ids and _id from the recording
        4. Append the recording to the list of recordings
        5. Replace the list of recording ids with the list of recordings
        6. Insert the completed songwriter into the SongwritersRecordings collection
    '''
    for i, songwriter in enumerate(songwriters):
        songwriter = loads(dumps(songwriter))       # fix formatting
        recordings = []
        for recording_id in songwriter["recordings"]:
            recording = recordings_collection.find({"recording_id": recording_id})
            recording = list(recording)[0]

            recording.pop("songwriter_ids")
            recording.pop("_id")
            recordings.append(recording)
        
        songwriter["recordings"] = recordings
        songwriter.pop("_id")
        # if i == 0: print(songwriter) # uncomment to see the first songwriter
        collection.insert_one(songwriter)

    db["recordings"].drop() # recordings database no longer needed
    
    client.close()

if __name__ == "__main__":
    # call main with port argument
    main(sys.argv[1:])