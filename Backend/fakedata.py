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
notification = Base.classes.notification
np = Base.classes.notification_provider
state = Base.classes.state
jurisdiction = Base.classes.jurisdiction
infectious_city = Base.classes.infectious_city
environment_city = Base.classes.environment_city
ns = session.query(notification)
d1 = datetime.strptime('1/1/2015 1:30 AM', '%m/%d/%Y %I:%M %p')
d2 = datetime.now()
to_add = []
count = 0
for n in ns:
    city_id = n.city_id
    city = session.query(infectious_city).filter(infectious_city.city_id == city_id)
    if city.count() == 0:
        city = session.query(environment_city).filter(environment_city.city_id == city_id)
    city = city.first()
    state_id = city.state_id
    jurs = session.query(jurisdiction).filter(jurisdiction.state_id == state_id)
    for jur in jurs:
        provider_id = jur.provider_id
        new_np = np(n_id = n.n_id, condition = 1, provider_id = provider_id)
        n.notified = 1
        to_add.append(new_np)
try:
    session.add_all(to_add)
    session.commit()
finally:
    session.close()
