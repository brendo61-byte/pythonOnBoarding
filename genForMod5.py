import datetime
import random
import json

def stuff(data):
    info = {}
    x = 0
    for name in data:
        status = thing()
        t0 = timeStuff()
        if x < 2:
            print(name)
            print(status)
            print(t0)
            x += 1
        info[name] = {"grade": status, "Time": t0.timestamp()}

    return info

def start():
    data = ["Amy", "Brad", "Alex", "Dillon", "Rhianna", "Sara", "Jordan", "Hannah", "Abi", "Sam", "Cat", "Tomas", "Ashly"]
    val = stuff(data=data)
    print(json.dumps(val, indent=4))

def thing():
    x = random.random()
    if x > 0.7:
        return None
    else:
        return random.randint(50, 101)


def timeStuff():
    year = 2019
    month = 11
    day = 1
    hour = getHour()
    min = random.randint(0, 60)
    sec = random.randint(0, 60)

    if hour < 10:
        day = 2

    return datetime.datetime(year=year, month=month, day=day, minute=min, second=sec)

def getHour():
    if thing():
        return random.randint(18, 24)
    else:
        return random.randint(0, 5)

if __name__ == '__main__':
    start()
