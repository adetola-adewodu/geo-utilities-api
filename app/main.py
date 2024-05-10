from dotenv import load_dotenv
import structlog
from fastapi import FastAPI, Depends
from app import queries

from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=queries.engine)

app = FastAPI(
    title="Geo Utilities API",
    description="Rest api for utilities",
    version="0.0.1",
)

load_dotenv()

log = structlog.get_logger()

# Dependency for session
def get_db():
    """Get Database Session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get(
    "/",
    summary="Checks if API is running",
    description="returns a message to make sure service is up and running",
)
def read_root():
    """Returns message that service is up and running"""
    return {"Geo Utilities API": "Running"}


@app.get(
    "/nearest",
    summary="Check if point is near to other points",
    description="returns the nearest points given a point",
    tags=["Basic Geo"],
)
def get_nearest(
    longitude: float,
    latitude: float,
    k_nearest_neighbor: int,
    db: Session = Depends(get_db),
):
    """Returns message that service is up and running"""
    return queries.get_nearest_neighbors(db, longitude, latitude, k_nearest_neighbor)


@app.get(
    "/within",
    summary="Checks if point is within geofence",
    description="returns if a point is within a geofence",
    tags=["Basic Geo"],
)
def get_within_location(
    longitude: float,
    latitude: float,
    db: Session = Depends(get_db),
):
    """Returns message that service is up and running"""
    return queries.within_location(db, longitude, latitude)


# Ev Stations
@app.get(
    "/evstations",
    summary="Get all the evstations",
    description="returns all the evstations",
    tags=["EV Station"],
)
def evstation_list(db: Session = Depends(get_db)):
    """Get a lists of stations"""
    skip = 0
    limit = 10
    return queries.get_evstations(db, skip, limit)


@app.get(
    "/evstation/{id}",
    summary="Get a ev station given an id",
    description="return a evstation given an id",
    tags=["EV Station"],
)
def evstation_detail(id: int, db: Session = Depends(get_db)):
    """Givens detail of the evstation in json"""
    return queries.get_evstation(id, db)


# Powerlines
@app.get(
    "/powerlines",
    summary="Get all the powerlines",
    description="returns all the powerlines",
    tags=["Power Line"],
)
def powerlines_list(db: Session = Depends(get_db)):
    """Get a lists of powerlines"""
    skip = 0
    limit = 10

    return queries.get_powerlines(db, skip, limit)


@app.get(
    "/powerline/{id}",
    summary="Get a powerline given an id",
    description="return a powerline given an id",
    tags=["Power Line"],
)
def powerline_detail(id: int, db: Session = Depends(get_db)):
    """Givens detail of the powerline in json"""
    return queries.get_powerline(id, db)


# PowerPlants
@app.get(
    "/powerplant",
    summary="Get all the powerplants",
    description="returns all the powerplants",
    tags=["Power Plant"],
)
def powerplant_list(db: Session = Depends(get_db)):
    """Get a lists of stations"""
    skip = 0
    limit = 10

    return queries.get_powerplants(db, skip, limit)


@app.get(
    "/powerplant/{id}",
    summary="Get a powerplant given an id",
    description="return a powerplant given an id",
    tags=["Power Plant"],
)
def powerplant_detail(id: int, db: Session = Depends(get_db)):
    """Givens detail of the station in json"""
    return queries.get_powerplant(id, db)


# PublicPower
@app.get(
    "/publicpower",
    summary="Get all the publicpower",
    description="returns all the publicpower",
    tags=["Public Power"],
)
def publicpower_list(db: Session = Depends(get_db)):
    """Get a lists of publicpowers"""
    skip = 0
    limit = 10
    return queries.get_publicpowers(db, skip, limit)


@app.get(
    "/publicpower/{id}",
    summary="Get a publicpower given an id",
    description="return a publicpower given an id",
    tags=["Public Power"],
)
def publicpower_detail(id: int, db: Session = Depends(get_db)):
    """Givens detail of the station in json"""
    return queries.get_publicpower(id, db)


# substations
@app.get(
    "/substations",
    summary="Get all the stations",
    tags=["Sub Stations"],
    description="returns all the stations",
)
def substation_list(db: Session = Depends(get_db)):
    """Get a lists of stations"""
    skip = 0
    limit = 10
    return queries.get_substations(db, skip, limit)


@app.get(
    "/substation/{id}",
    summary="Get a station given an id",
    tags=["Sub Stations"],
    description="return a station given an id",
)
def substations_detail(id: int, db: Session = Depends(get_db)):
    """Givens detail of the station in json"""
    return queries.get_substation(id, db)
