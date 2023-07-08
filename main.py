import datetime
import json
import random
import string

today = datetime.datetime.strptime("2023-06-30 06:00:00", "%Y-%m-%d %H:%M:%S")
yesterday = today - datetime.timedelta(days=1)

finalData = []
data = ""

color = {
    0: '#FF0000',  # Red
    1: '#FF1A00',
    2: '#FF3500',
    3: '#FF5000',
    4: '#FF6B00',
    5: '#FF8600',
    6: '#FFA100',
    7: '#FFBC00',
    8: '#FFD700',
    9: '#FFF200',
    10: '#E2FF00'  # Green
}

with open('ahmedabad.json', 'r') as f:
    data = json.load(f)['features']


def translate(x, a, b, c, d):
    y = (x-a)/(b-a)*(d-c)+c
    return int(y)


for object in data:
    values = {}
    tempL = []

    for location in object["geometry"]["coordinates"][0]:
        tempL.append([location[1], location[0]])

    for i in range(24):
        currentTime = int(
            (yesterday + datetime.timedelta(hours=i)).timestamp())
        ws = random.randint(1, 10)
        temp = random.randint(25, 40)
        p4 = random.randint(300, 500)
        p2 = random.randint(300, 500)
        hum = random.randint(1, 100)
        values[str(currentTime)] = {
            "ws": {
                "value": ws,
                "color": color[ws],
            },
            "temp": {
                "value": temp,
                "color": color[translate(temp, 25, 40, 0, 10)],
            },
            "p4": {
                "value": p4,
                "color": color[translate(p4, 300, 500, 0, 10)],
            },
            "p2": {
                "value": p2,
                "color": color[translate(p2, 300, 500, 0, 10)],
            },
            "hum": {
                "value": hum,
                "color": color[translate(hum, 0, 100, 0, 10)],
            },
        }

    finalData.append({
        "deviceId": ''.join(random.choices(string.ascii_uppercase +
                                           string.digits, k=7)),
        "location": tempL,
        "values": values
    })

file_path = "values.json"

with open(file_path, 'w') as json_file:
    json_file.write(json.dumps(finalData, indent=4))
