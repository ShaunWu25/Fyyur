from models import *
from app import db, app
import sys

venues_data=[{
    "city": "San Francisco",
    "state": "CA",
    "venues": [{
      "id": 1,
      "name": "The Musical Hop",
      "num_upcoming_shows": 0,
    }, {
      "id": 3,
      "name": "Park Square Live Music & Coffee",
      "num_upcoming_shows": 1,
    }]
  }, {
    "city": "New York",
    "state": "NY",
    "venues": [{
      "id": 2,
      "name": "The Dueling Pianos Bar",
      "num_upcoming_shows": 0,
    }]
}]

def create_venues_data(venues_data):
    try:
        error = False
        for data in venues_data:
            city = data['city']
            state = data["state"]
            for venue in data['venues']:
                id = venue['id']
                name = venue['name']

                venue_temp = Venue(id=id, name=name, city=city, state=state)
                db.session.add(venue_temp)
                db.session.commit()
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    
    finally:
        db.session.close()


create_venues_data(venues_data)