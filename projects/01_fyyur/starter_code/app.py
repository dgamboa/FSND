#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json
import dateutil.parser
import babel
from flask import (
  Flask,
  render_template,
  request,
  Response,
  flash,
  redirect,
  url_for
)
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
from flask_migrate import Migrate
import datetime

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)

# Connect to local postgresql database
# [x] Define migration and import Migrate module
migrate = Migrate(app, db)


#----------------------------------------------------------------------------#
# Import Models.
#----------------------------------------------------------------------------#

from models import *

#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format)

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  return render_template('pages/home.html')


#  Venues
#  ----------------------------------------------------------------

# List venues grouped by city
@app.route('/venues')
def venues():
  unique_areas = Venue.query.distinct('city','state').all()
  areas = []

  for area in unique_areas:
    venues = Venue.query.filter(Venue.city == area.city, Venue.state == area.state).all()
    record = {
      'city': area.city,
      'state': area.state,
      'venues': venues,
    }
    areas.append(record)

  return render_template('pages/venues.html', areas=areas)

# Case-insensitive search for venues
@app.route('/venues/search', methods=['POST'])
def search_venues():
  search_term = request.form.get('search_term')
  venues = Venue.query.filter(Venue.name.ilike('%' + search_term + '%'))
  data = []

  for venue in venues:
    record = {"id": venue.id, "name": venue.name}
    data.append(record)

  results = {"count": venues.count(), "data": data}

  return render_template('pages/search_venues.html', results=results, search_term=search_term)

# Detailed page for a specific venue
@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  venues = Venue.query.join(Venue.shows, isouter=True).all()
  now = datetime.datetime.now()
  present_date = datetime.date(now.year, now.month, now.day)
  venues_list = []

  for venue in venues:
    upcoming_shows = []
    past_shows = []
    upcoming_shows_count = 0
    past_shows_count = 0
    for show in venue.shows:
      if show.start_time > present_date:
        upcoming_shows_count += 1
        upcoming_show_record = {
          "artist_id": show.artist_id,
          "artist_name": Artist.query.get(show.artist_id).name,
          "artist_image_link": Artist.query.get(show.artist_id).image_link,
          "start_time": str(show.start_time),
        }
        upcoming_shows.append(upcoming_show_record)
      else:
        past_shows_count += 1
        past_show_record = {
          "artist_id": show.artist_id,
          "artist_name": Artist.query.get(show.artist_id).name,
          "artist_image_link": Artist.query.get(show.artist_id).image_link,
          "start_time": str(show.start_time),
        }
        past_shows.append(past_show_record)
    venue_record = {
      "id": venue.id,
      "name": venue.name,
      "genres": venue.genres,
      "address": venue.address,
      "city": venue.city,
      "state": venue.state,
      "phone": venue.phone,
      "website": venue.website,
      "facebook_link": venue.facebook_link,
      "seeking_talent": venue.seeking_talent,
      "image_link": venue.image_link,
      "past_shows": past_shows,
      "upcoming_shows": upcoming_shows,
      "past_shows_count": str(past_shows_count),
      "upcoming_shows_count": str(upcoming_shows_count),
    }
    venues_list.append(venue_record)

  data = list(filter(lambda d: d['id'] == venue_id, venues_list))[0]

  return render_template('pages/show_venue.html', venue=data)


#  Create Venue
#  ----------------------------------------------------------------

# Retrieve a form to create a venue and display it
@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)

# Submit a form to create a venue and record it
@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
  form = VenueForm(request.form)
  if form.validate_on_submit():
    error = False
    try:
      venue = Venue(
      name=request.form.get('name'),
      city=request.form.get('city'),
      state=request.form.get('state'),
      address=request.form.get('address'),
      phone=request.form.get('phone'),
      genres=request.form.getlist('genres'),
      website=request.form.get('website'),
      facebook_link=request.form.get('facebook_link')
      )
      db.session.add(venue)
      db.session.commit()
    except Exception as e:
      error = True
      db.session.rollback()
      print(f'Error ==> {e}')
    finally:
      db.session.close()
    if error:
      # [x] On unsuccessful db insert, flash an error
      flash('Error: Venue ' + request.form['name'] + ' was not listed. Please check your inputs and try again :)')
    else:
      # on successful db insert, flash success
      flash(request.form['name'] + ' was successfully listed!')
  else:
    errors_list = []
    for error in form.errors.values():
      errors_list.append(error[0])
    flash('Invalid submission: \n' + ', '.join(errors_list))
    return render_template('forms/new_venue.html', form=form)

  venue_id = Venue.query.order_by(db.desc(Venue.id)).all()[0].id
  return redirect(url_for('show_venue', venue_id=venue_id))

# Delete a venue
@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
  error = False
  try:
    venue_to_delete = Venue.query.get(venue_id)
    db.session.delete(venue_to_delete)
    db.session.commit()
  except Exception as e:
    error = True
    db.session.rollback()
    print(f'Error ==> {e}')
  finally:
    db.session.close()
  if error:
    # On unsuccessful db delete, flash an error
    flash('Error: Venue was not deleted. Please check your process and try again :)')
  else:
    # On successful db delete, flash success
    flash('Venue was successfully deleted!')

  return None

#  Artists
#  ----------------------------------------------------------------

# Disaply a list of all artists
@app.route('/artists')
def artists():
  artists = Artist.query.all()
  return render_template('pages/artists.html', artists=artists)

# Case-insensitive search for artists
@app.route('/artists/search', methods=['POST'])
def search_artists():
  search_term = request.form.get('search_term')
  artists = Artist.query.filter(Artist.name.ilike('%' + search_term + '%'))
  data = []

  for artist in artists:
    record = {"id": artist.id, "name": artist.name}
    data.append(record)

  results = {"count": artists.count(), "data": data}

  return render_template('pages/search_artists.html', results=results, search_term=search_term)

# Detailed page for a specific artist
@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  # shows the artist page with the given artist_id
  # [x] Replace with real artist data from the artists table, using artist_id

  artists = Artist.query.join(Artist.shows, isouter=True).all()
  now = datetime.datetime.now()
  present_date = datetime.date(now.year, now.month, now.day)
  artists_list = []

  for artist in artists:
    upcoming_shows = []
    past_shows = []
    upcoming_shows_count = 0
    past_shows_count = 0
    for show in artist.shows:
      if show.start_time > present_date:
        upcoming_shows_count += 1
        upcoming_show_record = {
          "venue_id": show.venue_id,
          "venue_name": Venue.query.get(show.venue_id).name,
          "venue_image_link": Venue.query.get(show.venue_id).image_link,
          "start_time": str(show.start_time),
        }
        upcoming_shows.append(upcoming_show_record)
      else:
        past_shows_count += 1
        past_show_record = {
          "venue_id": show.venue_id,
          "venue_name": Venue.query.get(show.venue_id).name,
          "venue_image_link": Venue.query.get(show.venue_id).image_link,
          "start_time": str(show.start_time),
        }
        past_shows.append(past_show_record)
    artist_record = {
      "id": artist.id,
      "name": artist.name,
      "genres": artist.genres,
      "city": artist.city,
      "state": artist.state,
      "phone": artist.phone,
      "facebook_link": artist.facebook_link,
      "website": artist.website,
      "seeking_venue": artist.seeking_venue,
      "image_link": artist.image_link,
      "past_shows": past_shows,
      "upcoming_shows": upcoming_shows,
      "past_shows_count": str(past_shows_count),
      "upcoming_shows_count": str(upcoming_shows_count),
    }
    artists_list.append(artist_record)

  data = list(filter(lambda d: d['id'] == artist_id, artists_list))[0]

  return render_template('pages/show_artist.html', artist=data)

#  Update
#  ----------------------------------------------------------------

# Create a form to edit an artist record and populate it with existing data
@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  artist = Artist.query.get(artist_id)
  form = ArtistForm(obj=artist)

  return render_template('forms/edit_artist.html', form=form, artist=artist)

# Submit the edits for an artist and record them
@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  error = False
  artist = Artist.query.get(artist_id)
  form = ArtistForm(request.form)
  try:
    artist.name=form.name.data
    artist.city=form.city.data
    artist.state=form.state.data
    artist.phone=form.phone.data
    artist.genres=form.genres.data
    artist.facebook_link=form.facebook_link.data
    db.session.add(artist)
    db.session.commit()
  except Exception as e:
    error = True
    db.session.rollback()
    print(f'Error ==> {e}')
  finally:
    db.session.close()
  if error:
    # On unsuccessful db update, flash an error
    flash('Error: Artist ' + request.form['name'] + ' was not updated. Please check your inputs and try again :)')
  else:
    # On successful db update, flash success
    flash(request.form['name'] + ' was successfully updated!')

  return redirect(url_for('show_artist', artist_id=artist_id))

# Create a form to edit a venue and populate it with existing data
@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  venue = Venue.query.get(venue_id)
  form = VenueForm(obj=venue)

  return render_template('forms/edit_venue.html', form=form, venue=venue)

# Submit the edits for a venue and record them
@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  error = False
  venue = Venue.query.get(venue_id)
  try:
    venue.name=request.form.get('name')
    venue.city=request.form.get('city')
    venue.state=request.form.get('state')
    venue.address=request.form.get('address')
    venue.phone=request.form.get('phone')
    venue.genres=request.form.getlist('genres')
    venue.facebook_link=request.form.get('facebook_link')
    db.session.add(venue)
    db.session.commit()
  except Exception as e:
    error = True
    db.session.rollback()
    print(f'Error ==> {e}')
  finally:
    db.session.close()
  if error:
    # On unsuccessful db update, flash an error
    flash('Error: Venue ' + request.form['name'] + ' was not updated. Please check your inputs and try again :)')
  else:
    # On successful db update, flash success
    flash(request.form['name'] + ' was successfully updated!')

  return redirect(url_for('show_venue', venue_id=venue_id))

#  Create Artist
#  ----------------------------------------------------------------

# Retrieve a form to create an artist and display it
@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

# Submit a form to create an artist and record it
@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  form = ArtistForm(request.form)
  if form.validate_on_submit():
    error = False
    try:
      artist = Artist(
      name=request.form.get('name'),
      city=request.form.get('city'),
      state=request.form.get('state'),
      phone=request.form.get('phone'),
      genres=request.form.getlist('genres'),
      facebook_link=request.form.get('facebook_link')
      )
      db.session.add(artist)
      db.session.commit()
    except Exception as e:
      error = True
      db.session.rollback()
      print(f'Error ==> {e}')
    finally:
      db.session.close()
    if error:
      # On unsuccessful db insert, flash an error
      flash('Error: Artist ' + request.form['name'] + ' was not listed. Please check your inputs and try again :)')
    else:
      # On successful db insert, flash success
      flash(request.form['name'] + ' was successfully listed!')
  else:
    errors_list = []
    for error in form.errors.values():
      errors_list.append(error[0])
    flash('Invalid submission: \n' + ', '.join(errors_list))
    return render_template('forms/new_artist.html', form=form)

  artist_id = Artist.query.order_by(db.desc(Artist.id)).all()[0].id
  return redirect(url_for('show_artist', artist_id=artist_id))

# Delete an artist record
@app.route('/artists/<artist_id>', methods=['DELETE'])
def delete_artist(artist_id):
  error = False
  try:
    artist_to_delete = Artist.query.get(artist_id)
    db.session.delete(artist_to_delete)
    db.session.commit()
  except Exception as e:
    error = True
    db.session.rollback()
    print(f'Error ==> {e}')
  finally:
    db.session.close()
  if error:
    # On unsuccessful db delete, flash an error
    flash('Error: Artist was not deleted. Please check your process and try again :)')
  else:
    # On successful db delete, flash success
    flash('Artist was successfully deleted!')

  return None

#  Shows
#  ----------------------------------------------------------------

# Render a list of shows
@app.route('/shows')
def shows():
  shows = Show.query.join(Show.venue).join(Show.artist).all()
  shows_data = []
  for show in shows:
    record = {
      "venue_id": show.venue_id,
      "venue_name": show.venue.name,
      "artist_id": show.artist_id,
      "artist_name": show.artist.name,
      "artist_image_link": show.artist.image_link,
      "start_time": str(show.start_time)
    }
    shows_data.append(record)

  return render_template('pages/shows.html', shows=shows_data)

# Display form to create a show with an artist id and a venue id
@app.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

# Create a show based on the form submission and record it
@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  error = False
  try:
    show = Show(
    artist_id=request.form.get('artist_id'),
    venue_id=request.form.get('venue_id'),
    start_time=request.form.get('start_time')
    )
    db.session.add(show)
    db.session.commit()
  except Exception as e:
    error = True
    print(f'Error ==> {e}')
    db.session.rollback()
  finally:
    db.session.close()
  if error:
    # On unsuccessful db insert, flash an error
    flash('An error occurred. Show could not be listed.')
  else:
    # On successful db insert, flash success
    flash('Show was successfully listed!')

  return render_template('pages/home.html')


#----------------------------------------------------------------------------#
# Error Handlers.
#----------------------------------------------------------------------------#

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()
