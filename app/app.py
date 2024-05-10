import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

import structlog

import queries

log = structlog.get_logger()

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)

load_dotenv()

connection_string = (
    "postgresql://"
    + os.getenv("DB_USERNAME")
    + ":"
    + os.getenv("DB_PASSWORD")
    + "@"
    + os.getenv("DB_HOST")
    + ":"
    + os.getenv("DB_PORT")
    + "/"
    + os.getenv("DB_NAME")
)

app.config["SQLALCHEMY_DATABASE_URI"] = connection_string

log.info(connection_string)

db.init_app(app)


@app.route("/")
def root():
    """Returns message that service is up and running"""
    return {"Geo Utilities API": "Running"}



@app.route("/stations")
def station_list():
    """Get a lists of stations"""
    skip = 0
    limit = 10
    stations = queries.get_substations(db.session, skip, limit)
    log.info(stations)
    results = [[station.x, station.y] for station in stations]
    log.info(results)
    json_compatible_item_data = jsonify(results)
    return json_compatible_item_data

@app.route("/stations")
def stations(stations):
    """ Get stations """
    for station in stations:
        print(station)
    return stations

@app.route("/station/<id>")
def stations_detail(id):
    """Get the station detials given an id"""
    station = queries.get_substation(id, db.session)
    json_compatible_item_data = jsonify([station.x, station.y])
    return json_compatible_item_data


if __name__ == "__main__":

    app.debug = True
    app.run()
