from pymongo import MongoClient
import json
from bson.json_util import loads, dumps
import sys

def main(argv):
    with open('recordings.json', 'rb') as f1:
        recordings = json.load(f1)

    with open('songwriters.json', 'rb') as f2:
        songwriters = json.load(f2)

    # get port from argument and connect to server
    serverport = argv[0]
    client = MongoClient("mongodb://localhost:" + serverport)
    db = client["A4dbNorm"]

    # create recording and songwriter collections
    recordings_collection = db["recordings"]
    songwriters_collection = db["songwriters"]

    # delete existing collections (if they exist)
    recordings_collection.delete_many({})
    songwriters_collection.delete_many({})

    # fill recordings collection
    for record in recordings:
        record = loads(dumps(record))       # fix formatting
        ret_writer = recordings_collection.insert_one(record)

    # fill songwriters collection
    for writer in songwriters:
        writer = loads(dumps(writer))       # fix formatting
        ret_writer = songwriters_collection.insert_one(writer)

    client.close()


if __name__ == "__main__":
    # call main with port argument
    main(sys.argv[1:])