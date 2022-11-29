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
    print(random_second)
    return start + timedelta(seconds=random_second)

db_engine = create_engine('sqlite:///codecare.sqlite?check_same_thread=False')
Base = automap_base()
Base.prepare(autoload_with=db_engine)
sqlalchemy.orm.configure_mappers()
session= Session(db_engine)
record = Base.classes.location_record
state = Base.classes.state
rs = session.query(record)
d1 = datetime.strptime('1/1/2015 1:30 AM', '%m/%d/%Y %I:%M %p')
d2 = datetime.now()
to_add = []
count = 0
for r in rs:
    print(count)
    lat = r.latitude
    lon = r.longitude
    response = requests.get("https://api.3geonames.org/%f,%f.json"%(lat,lon)).text
    data = json.loads(response)
    state_name = data['nearest']['prov']
    print(data)
    print(state_name)
    state_id = session.query(state).filter(state.state_name == state_name).first().state_id
    r.state_id = state_id
    count += 1
try:
    session.commit()
finally:
    session.close()


  