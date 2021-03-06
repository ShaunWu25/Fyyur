from models import *
from app import db, app
import sys
from sqlalchemy.exc import IntegrityError
from sqlalchemy.dialects.mysql import insert

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
def create_venues_data(datas):
    try:
        error = False
        for data in datas:
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

#------------------------------------------------------------------------------------------------------
data1={
    "id": 1,
    "name": "The Musical Hop",
    "genres": ["Jazz", "Reggae", "Swing", "Classical", "Folk"],
    "address": "1015 Folsom Street",
    "city": "San Francisco",
    "state": "CA",
    "phone": "123-123-1234",
    "website": "https://www.themusicalhop.com",
    "facebook_link": "https://www.facebook.com/TheMusicalHop",
    "seeking_talent": True,
    "seeking_description": "We are on the lookout for a local artist to play every two weeks. Please call us.",
    "image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
    "past_shows": [{
      "artist_id": 4,
      "artist_name": "Guns N Petals",
      "artist_image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
      "start_time": "2019-05-21T21:30:00.000Z"
    }],
    "upcoming_shows": [],
    "past_shows_count": 1,
    "upcoming_shows_count": 0,
}

data2={
"id": 2,
"name": "The Dueling Pianos Bar",
"genres": ["Classical", "R&B", "Hip-Hop"],
"address": "335 Delancey Street",
"city": "New York",
"state": "NY",
"phone": "914-003-1132",
"website": "https://www.theduelingpianos.com",
"facebook_link": "https://www.facebook.com/theduelingpianos",
"seeking_talent": False,
"image_link": "https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80",
"past_shows": [],
"upcoming_shows": [],
"past_shows_count": 0,
"upcoming_shows_count": 0,
}

data3={
"id": 3,
"name": "Park Square Live Music & Coffee",
"genres": ["Rock n Roll", "Jazz", "Classical", "Folk"],
"address": "34 Whiskey Moore Ave",
"city": "San Francisco",
"state": "CA",
"phone": "415-000-1234",
"website": "https://www.parksquarelivemusicandcoffee.com",
"facebook_link": "https://www.facebook.com/ParkSquareLiveMusicAndCoffee",
"seeking_talent": False,
"image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
"past_shows": [{
    "artist_id": 5,
    "artist_name": "Matt Quevedo",
    "artist_image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
    "start_time": "2019-06-15T23:00:00.000Z"
}],
"upcoming_shows": [{
    "artist_id": 6,
    "artist_name": "The Wild Sax Band",
    "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
    "start_time": "2035-04-01T20:00:00.000Z"
}, {
    "artist_id": 6,
    "artist_name": "The Wild Sax Band",
    "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
    "start_time": "2035-04-08T20:00:00.000Z"
}, {
    "artist_id": 6,
    "artist_name": "The Wild Sax Band",
    "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
    "start_time": "2035-04-15T20:00:00.000Z"
}],
"past_shows_count": 1,
"upcoming_shows_count": 1,
}

show_venue_datas = [data1, data2, data3]
def create_show_venue_datas(datas):
    try:
        error = False
        for data in datas:
            try:
                error02 = False

                id = data['id']
                genres = data['genres']
                address = data["address"]
                phone = data["phone"]
                website = data["website"]
                facebook_link = data["facebook_link"]
                seeking_talent = data["seeking_talent"]
                image_link = data["image_link"]

                if "seeking_description" in data:
                    seeking_description = data["seeking_description"]
                    print("seeking_description existed")
                else:
                    seeking_description = 'NA'
                
                row_data = Venue.query.filter(Venue.id == id).one()
                row_data.genres = genres
                row_data.address = address
                row_data.phone = phone
                row_data.website = website
                row_data.facebook_link = facebook_link
                row_data.seeking_talent = seeking_talent
                row_data.image_link = image_link
                row_data.seeking_description = seeking_description

                db.session.commit()
            except:
                error02 = True
                db.session.rollback()
                print("in" + sys.exc_info())
            
            finally:
                db.session.close()
    except:
        error = True
        db.session.rollback()
        print("out" + sys.exc_info())
    
    finally:
        db.session.close()

artist_data = []
data4={
    "id": 4,
    "name": "Guns N Petals",
    "genres": ["Rock n Roll"],
    "city": "San Francisco",
    "state": "CA",
    "phone": "326-123-5000",
    "website": "https://www.gunsnpetalsband.com",
    "facebook_link": "https://www.facebook.com/GunsNPetals",
    "seeking_venue": True,
    "seeking_description": "Looking for shows to perform at in the San Francisco Bay Area!",
    "image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
    "past_shows": [{
      "venue_id": 1,
      "venue_name": "The Musical Hop",
      "venue_image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
      "start_time": "2019-05-21T21:30:00.000Z"
    }],
    "upcoming_shows": [],
    "past_shows_count": 1,
    "upcoming_shows_count": 0,
  }
data5={
"id": 5,
"name": "Matt Quevedo",
"genres": ["Jazz"],
"city": "New York",
"state": "NY",
"phone": "300-400-5000",
"facebook_link": "https://www.facebook.com/mattquevedo923251523",
"seeking_venue": False,
"image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
"past_shows": [{
    "venue_id": 3,
    "venue_name": "Park Square Live Music & Coffee",
    "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
    "start_time": "2019-06-15T23:00:00.000Z"
}],
"upcoming_shows": [],
"past_shows_count": 1,
"upcoming_shows_count": 0,
}
data6={
"id": 6,
"name": "The Wild Sax Band",
"genres": ["Jazz", "Classical"],
"city": "San Francisco",
"state": "CA",
"phone": "432-325-5432",
"seeking_venue": False,
"image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
"past_shows": [],
"upcoming_shows": [{
    "venue_id": 3,
    "venue_name": "Park Square Live Music & Coffee",
    "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
    "start_time": "2035-04-01T20:00:00.000Z"
}, {
    "venue_id": 3,
    "venue_name": "Park Square Live Music & Coffee",
    "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
    "start_time": "2035-04-08T20:00:00.000Z"
}, {
    "venue_id": 3,
    "venue_name": "Park Square Live Music & Coffee",
    "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
    "start_time": "2035-04-15T20:00:00.000Z"
}],
"past_shows_count": 0,
"upcoming_shows_count": 3,
}
artist_data = [data4, data5, data6]
def create_artist_data(datas):
    try:
        error = False
        for data in datas:
            id = data['id']
            name = data['name']
            genres = data['genres']
            city = data['city']
            state = data["state"]
            phone = data["phone"]
            seeking_venue = data["seeking_venue"]
            image_link = data["image_link"]
            if "website" in data:
                website = data["website"]
                print("website existed")
            else:
                website = 'NA'

            atist_temp = Artist(id=id, name=name, city=city, state=state, phone=phone, seeking_venue=seeking_venue,
            image_link=image_link, website = website)
            db.session.add(atist_temp)
            db.session.commit()
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    
    finally:
        db.session.close()

show_data=[{
    "venue_id": 1,
    "venue_name": "The Musical Hop",
    "artist_id": 4,
    "artist_name": "Guns N Petals",
    "artist_image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
    "start_time": "2019-05-21T21:30:00.000Z"
  }, {
    "venue_id": 3,
    "venue_name": "Park Square Live Music & Coffee",
    "artist_id": 5,
    "artist_name": "Matt Quevedo",
    "artist_image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
    "start_time": "2019-06-15T23:00:00.000Z"
  }, {
    "venue_id": 3,
    "venue_name": "Park Square Live Music & Coffee",
    "artist_id": 6,
    "artist_name": "The Wild Sax Band",
    "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
    "start_time": "2035-04-01T20:00:00.000Z"
  }, {
    "venue_id": 3,
    "venue_name": "Park Square Live Music & Coffee",
    "artist_id": 6,
    "artist_name": "The Wild Sax Band",
    "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
    "start_time": "2035-04-08T20:00:00.000Z"
  }, {
    "venue_id": 3,
    "venue_name": "Park Square Live Music & Coffee",
    "artist_id": 6,
    "artist_name": "The Wild Sax Band",
    "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
    "start_time": "2035-04-15T20:00:00.000Z"
  }]

def create_show_data(datas):
    try:
        error = False
        for data in datas:
            venue_id = data['venue_id']
            artist_id = data['artist_id']
            start_time = data['start_time']

            show_temp = Show(venue_id=venue_id, artist_id=artist_id, start_time=start_time)
            db.session.add(show_temp)
            db.session.commit()
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    
    finally:
        db.session.close()
#------------------------------------------------------------------------------------------------------------------------------------


# Default port:
if __name__ == '__main__':
    # create_venues_data(venues_data)
    # create_show_venue_datas(show_venue_datas)
    # create_artist_data(artist_data)
    create_show_data(show_data)
