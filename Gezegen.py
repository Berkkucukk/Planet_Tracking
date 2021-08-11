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

        print("Jüpiter şuan Dünyaya en yakın konumunda :)")

    else:
        print("Jüpiter malesef yakınlarda gözükmüyor :(")


def Saturn():
    last_date=datetime.date(2020,8,1)
    while int(last_date.year)<int(year):
        last_date=last_date + datetime.timedelta(days=340)

    if last_date.month==month :

        print("Satürn şuan Dünyaya en yakın konumunda :)")

    else:
        print("Satürn malesef yakınlarda gözükmüyor :(")

def Neptun():
    last_date=datetime.date(2020,9,8)
    while int(last_date.year)<int(year):
        last_date=last_date + datetime.timedelta(days=362)

    if last_date.month==month :

        print("Neptün şuan Dünyaya en yakın konumunda :)")

    else:
        print("Neptün malesef yakınlarda gözükmüyor :(")

def Uranus():
    last_date=datetime.date(2020,11,5)
    while int(last_date.year)<int(year):
        last_date=last_date + datetime.timedelta(days=360)

    if last_date.month==month :

        print("Uranüs şuan Dünyaya en yakın konumunda :)")

    else:
        print("Uranüs malesef yakınlarda gözükmüyor :(")

def Merkur():
    last_date=datetime.date(2020,10,5)
    while int(last_date.year)<int(year):
        last_date=last_date + datetime.timedelta(days=120)

    if last_date.month==month :

        print("Merkür şuan Dünyaya en yakın konumunda :)")

    else:
        print("Merkür malesef yakınlarda gözükmüyor :(")

def Mars():
    last_date=datetime.date(2018,10,5)
    while int(last_date.year)<int(year):
        last_date=last_date + datetime.timedelta(days=750)

    if last_date.month==month and last_date.year==year :

        print("Mars şuan Dünyaya en yakın konumunda :)")

    else:
        print("Mars malesef yakınlarda gözükmüyor :(")
Jupiter()
Saturn()
Neptun()
Uranus()
Merkur()
Mars()
