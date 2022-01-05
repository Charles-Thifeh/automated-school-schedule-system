import datetime

def todayAt (hr, min=0, sec=0, micros=0):
   now = datetime.datetime.now()
   return now.replace(hour=hr, minute=min, second=sec, microsecond=micros)

assembly = todayAt(7, 45, 00, 000000)


periodsch = 40
teabreak = 15
longbreak = 20
extbreak = 5
