from pymongo import MongoClient
import json

if __name__ == "__main__":
    with open('recordings.json', 'rb') as f1:
        recordings = json.load(f1)

    with open('songwriters.json', 'rb') as f2:
        songwriters = json.load(f2)

    client = MongoClient()
    db = client["A4dbNorm"]

    recordings_collection = db["recordings"]
    songwriters_collection = db["songwriters"]

    recordings_collection.delete_many({})
    songwriters_collection.delete_many({})

    for record in recordings:
        record.pop("_id")
        ret_writer = recordings_collection.insert_one(record)

    for writer in songwriters:
        writer.pop("_id")
        ret_writer = songwriters_collection.insert_one(writer)
