from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import sqlalchemy
from random import randrange
from random import randint
from datetime import timedelta
from datetime import datetime
import json
import requests
def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

db_engine = create_engine('sqlite:///codecare.sqlite?check_same_thread=False')
Base = automap_base()
Base.prepare(autoload_with=db_engine)
sqlalchemy.orm.configure_mappers()
session= Session(db_engine)
location_record = Base.classes.location_record
d1 = datetime.strptime('1/1/2019 1:30 AM', '%m/%d/%Y %I:%M %p')
d2 = datetime.now()
to_add = []
count = 0
for i in range(40):
    print(count)
    count += 1
    response = requests.get('https://api.3geonames.org/randomland.US.json').text
    data = json.loads(response)
    new_record = location_record(location_id = count, patient_id = randint(1,10), latitude = data['nearest']['latt'], longitude = data['nearest']['longt'], datetime = random_date(d1,d2).strftime("%m/%d/%Y, %H:%M:%S"), city = data['nearest']['city'])
    to_add.append(new_record)
try:
    session.add_all(to_add)
    session.commit()
finally:
    session.close()
