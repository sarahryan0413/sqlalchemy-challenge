# Import the dependencies.
import datetime as dt
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# Declare a Base using `automap_base()`
Base = automap_base()
# Use the Base class to reflect the database tables
Base.prepare(autoload_with=engine)

# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`
Measurement = Base.classes.measurement  #measurement table  
Station = Base.classes.station          #station table

# Create a session
session = Session(engine) 


#################################################
# Flask Setup
#################################################
app = Flask(__name__)   #initializes a Flask web application


#################################################
# Flask Routes
#################################################

# Set up a homepage route
@app.route("/")     #this says: “When someone visits the home page (/), run this function.”
def welcome():      #function name: welcome
    """List all available api routes."""   #docstring: just for developers reading the code
    return (
        f"Available Routes:<br/>"          #<br/> : line break
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date<br/>"
        f"/api/v1.0/start_date/end_date"
    )


# Create a precipitation route
@app.route("/api/v1.0/precipitation")
def percipitation():
    """Retrieve the last 12 months of precipitation data"""
    # Calculate the date one year from the last date in data set.
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    precipitation_scores = session.query(Measurement.date, Measurement.prcp)\
                              .filter(Measurement.date >= year_ago).all()
    session.close()

    # Create dictionary using date as the key and prcp as the value.
    precipitation_dict = {date: prcp for date, prcp in precipitation_scores}
    return jsonify(precipitation_dict)


# Create a stations route
@app.route("/api/v1.0/stations")
def stations():
    """Retrieve a list of all the stations"""
    stations = session.query(Station.station).all()
    session.close()

    # Unravel (using np.ravel) results into a 1D array and convert to a list
    station_results = list(np.ravel(stations))
    return jsonify(stations=station_results)


# Create a temperature observations route
@app.route("/api/v1.0/tobs")
def tobs():
    """Retrieves dates and temperature observations from the most-active station (USC00519281) for the past year"""
    # Calculate the date one year from the last date in data set.
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    # Perform a query to retrieve the data and precipitation scores
    query_results = session.query(Measurement.tobs)\
                              .filter(Measurement.station == 'USC00519281')\
                              .filter(Measurement.date >= year_ago).all()
    session.close()

    # Unravel (using np.ravel) results into a 1D array and convert to a list
    most_active_station_results = list(np.ravel(query_results))
    return jsonify(temperatures=most_active_station_results)


# Create a route for min, max, and avg temps before a specified start or start-end range
@app.route("/api/v1.0/start_date")
@app.route("/api/v1.0/start_date/end_date")
def temp_stats(start, end=None):     #start is mandatory, end=None means its not required
    """Return temperature min, max, and avg"""
    
    # select statement - creates a list of SQL functions to get min, max, and avg
    sel = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]

    if not end: 
        start = dt.datetime.strptime(start, "%m-%d-%y")    #converts start time string to a datetime object
        
        #calculate temp min, max, and avg for dates greater than start
        results = session.query(*sel).filter(Measurement.date>=start).all()
        session.close()

        #unravel results into a 1D array and convert to a list
        temps=list(np.ravel(results))
        return jsonify(temps)

    #calculate temp min,max, and avg with start and stop
    start = dt.datetime.strptime(start, "%m-%d-%y")
    end = dt.datetime.strptime(end, "%m-%d-%y")

    results = session.query(*sel).filter(Measurement.date>=start)\
                                 .filter(Measurement.date<=end).all()
    session.close()

    # Unravel (using np.ravel) results into a 1D array and convert to a list
    temps = list(np.ravel(results))
    return jsonify(temperatures=temps)


if __name__ == "__main__":
    app.run(debug=True)

