from pymongo import MongoClient
import json
from bson.json_util import loads, dumps

if __name__ == "__main__":
    with open('recordings.json', 'rb') as f1:
        recordings = json.load(f1)

    with open('songwriters.json', 'rb') as f2:
        songwriters = json.load(f2)

    client = MongoClient()
    db = client["A4dbNorm"]

    # create recording and songwriter collections
    recordings_collection = db["recordings"]
    songwriters_collection = db["songwriters"]

    # delete existing collections (if they exist)
    recordings_collection.delete_many({})
    songwriters_collection.delete_many({})

    for record in recordings:
        record = loads(dumps(record))
        ret_writer = recordings_collection.insert_one(record)

    for writer in songwriters:
        writer = loads(dumps(writer))
        ret_writer = songwriters_collection.insert_one(writer)

    client.close()
