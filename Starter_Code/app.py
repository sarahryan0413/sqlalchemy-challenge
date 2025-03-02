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
    return jsonify(station_results)



if __name__ == "__main__":
    app.run(debug=True)