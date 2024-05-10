import os
from dotenv import load_dotenv
import structlog
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# for flask use import models
from app import models

log = structlog.get_logger()
load_dotenv()
SQLALCHEMY_DATABASE_URL = (
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
# Add engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
Base = declarative_base()


def get_nearest_neighbors(session, longitude, latitude, k):
    """Return k nearest points to point(longitude, latitude)"""

    query_string = f"""select * from evstations
                        order by st_astext(wkb_geometry)
                <-> ST_Point({longitude}, {latitude}) limit {k}"""
    log.info(query_string)
    results = session.execute(query_string)
    return results.fetchall()


def within_location(session, longitude, latitude):
    """Return whether longitude/latitude in a geofence"""

    query_string = f"""SELECT * FROM powerlines WHERE
                        ST_DWithin(st_astext(wkb_geometry)::geography,
                        ST_Point({longitude}, {latitude})::geography,
                        1609.34) limit 1"""
    log.info(query_string)

    results = session.execute(query_string)
    return results.fetchall()


def get_evstations(session, skip, limit):
    """Get EV Stations"""
    evstations = session.query(models.Evstation).offset(skip).limit(limit).all()
    return evstations


def get_evstation(id, session):
    """Get a EV Station given an id"""
    station = (
        session.query(models.Evstation).filter(models.Evstation.ogc_fid == id).first()
    )
    log.info(station)
    return station


# Add Powerline
def get_powerlines(session, skip, limit):
    """Get Powerline"""
    powerlines = session.query(models.Powerline).offset(skip).limit(limit).all()
    return powerlines


def get_powerline(id, session):
    """Get a powerline given an id"""
    powerline = (
        session.query(models.Powerline).filter(models.Powerline.ogc_fid == id).first()
    )
    log.info(powerline)
    return powerline


# Add Powerplant
def get_powerplants(session, skip, limit):
    """Get Powerplants"""
    powerplants = session.query(models.Powerplant).offset(skip).limit(limit).all()
    return powerplants


def get_powerplant(id, session):
    """Get a powerplant given an id"""
    powerplants = (
        session.query(models.Powerplant).filter(models.Powerplant.ogc_fid == id).first()
    )
    log.info(powerplants)
    return powerplants


# Add Publicpower
def get_publicpowers(session, skip, limit):
    """Get Powerplants"""
    publicpowers = session.query(models.Publicpower).offset(skip).limit(limit).all()
    return publicpowers


def get_publicpower(id, session):
    """Get a powerplant given an id"""
    publicpowers = (
        session.query(models.Publicpower)
        .filter(models.Publicpower.ogc_fid == id)
        .first()
    )
    log.info(publicpowers)
    return publicpowers


def get_substations(session, skip, limit):
    """Get the stations"""
    stations = session.query(models.Substation).offset(skip).limit(limit).all()
    return stations


def get_substation(id, session):
    """Get a station given an id"""
    station = (
        session.query(models.Substation).filter(models.Substation.ogc_fid == id).first()
    )
    log.info(station)
    return station
