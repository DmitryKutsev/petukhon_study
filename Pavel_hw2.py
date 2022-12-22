import json
# import teempfile
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--key", required=True)
parser.add_argument("--val")

args = parser.parse_args()

def add_data():
    info = {}
    info[args.key] = args.val

    with open('first_db', 'r', encoding = 'utf-8') as file:
        current_db = json.load(file)
        if args.key in current_db:
            search_key = current_db.get(args.key)
            if type(search_key) == list:
                current_db[args.key].append(args.val)
            else:
                temp = current_db[args.key]
                current_db[args.key] = []
                current_db[args.key].append(temp)
                current_db[args.key].append(args.val)
        else:
            current_db.update(info)


    with open('first_db', 'w', encoding='utf-8') as file:
        json.dump(current_db, file, indent=3)

def read_data():
    with open('first_db', 'r', encoding = 'utf-8') as file:
        current_db = json.load(file)
        search_value = current_db.get(args.key, 'None')
        if type(search_value) == str:
            print(search_value)
        else:
            print(*search_value, sep=", ")

if args.val != None:
    add_data()
else:
    read_data()
