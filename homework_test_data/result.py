import csv
import json
from csv import  DictReader
from files import CSV_FILE_PATH
from files import JSON_FILE_PATH

result = []

with open(JSON_FILE_PATH, "r") as users:
    users_reader = json.loads(users.read())

    for user in users_reader:
        result.append({'name':user['name'],'gender':user['gender'],'address':user['address'],'age':user['age'], 'books':[]})

index = 0
with open(CSV_FILE_PATH, newline='') as books:
    list_books = DictReader(books)

    for book in list_books:
        result[index]['books'].append({'title':book['Title'],'author':book['Author'],'pages':book['Pages'],'genre':book['Genre']})
        index += 1
        if index >= len(result):
            index = 0

with open("result.json", "w") as f:
    s = json.dumps(result, indent=4)
    f.write(s)

