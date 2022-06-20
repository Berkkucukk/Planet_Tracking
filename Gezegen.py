import datetime
date = datetime.datetime.now()
year=date.year
month=date.month
day=date.day

def Jupiter():
    last_year=2014
    last_mounth=1
    times=year-last_year
    last_date=datetime.date(2020,7,25)
    while int(last_date.year)<int(year):
        last_date=last_date + datetime.timedelta(days=390)

    if last_date.month==month :

        print("Jupiter is currently closest to Earth :)")

    else:
        print("Jupiter is not closest to Earth right now :(")


def Saturn():
    last_date=datetime.date(2020,8,1)
    while int(last_date.year)<int(year):
        last_date=last_date + datetime.timedelta(days=340)

    if last_date.month==month :

        print("Saturn is currently closest to Earth :)")

    else:
        print("Saturn is not closest to Earth right now :(")

def Neptune():
    last_date=datetime.date(2020,9,8)
    while int(last_date.year)<int(year):
        last_date=last_date + datetime.timedelta(days=362)

    if last_date.month==month :

        print("Neptune is currently closest to Earth :)")

    else:
        print("Neptune is not closest to Earth right now :(")

def Uranus():
    last_date=datetime.date(2020,11,5)
    while int(last_date.year)<int(year):
        last_date=last_date + datetime.timedelta(days=360)

    if last_date.month==month :

        print("Uranus is currently closest to Earth :)")

    else:
        print("Uranus is not closest to Earth right now :(")

def Merkur():
    last_date=datetime.date(2020,10,5)
    while int(last_date.year)<int(year):
        last_date=last_date + datetime.timedelta(days=120)

    if last_date.month==month :

        print("Merkur is currently closest to Earth :)")

    else:
        print("Merkur is not closest to Earth right now :(")

def Mars():
    last_date=datetime.date(2018,10,5)
    while int(last_date.year)<int(year):
        last_date=last_date + datetime.timedelta(days=750)

    if last_date.month==month and last_date.year==year :

        print("Mars is currently closest to Earth :)")

    else:
        print("Mars is not closest to Earth right now :(")
Jupiter()
Saturn()
Neptune()
Uranus()
Merkur()
Mars()
