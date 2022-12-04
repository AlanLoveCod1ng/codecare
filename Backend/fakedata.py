from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import sqlalchemy
from random import randrange
from random import choice
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
Notification = Base.classes.notification
Service = Base.classes.service
City = Base.classes.city
services = session.query(Service).all()
ns = session.query(Notification)
d1 = datetime.strptime('1/1/2015 1:30 AM', '%m/%d/%Y %I:%M %p')
d2 = datetime.now()
to_add = []
count = 0
for n in ns:
    print(count)
    city_name = session.query(City).filter(City.city_id == n.city_id).first().city_name
    title = ": ".join([city_name, choice(services).service_name])
    n.title = title
    count += 1
try:
    session.commit()
finally:
    session.close()


  