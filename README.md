# Geo Utilities API

## Install Gdal
brew install gdal

## Create and load geojson based tables into Postgres
ogr2ogr -f PostgreSQL PG:"dbname=postgres user=postgres password=mypassword" EVstations.json -nln evstations

## Example PostGIS Queries

select st_astext(wkb_geometry) from substations s order by st_astext(wkb_geometry) 
<-> ST_Point(-73.39993423899995, 43.89050742300003) limit 5


SELECT 'Feature' as type, row_to_json((SELECT l FROM ( select s.objectid, s.ogc_fid, s.subname, s.operator, s.operatorid) as l)) 
            as properties,st_asgeojson(wkb_geometry)::json as geometry from substations s
            

select st_astext(wkb_geometry) from powerlines p -- lines

select st_astext(wkb_geometry) from powerplants p -- points

SELECT * FROM powerlines WHERE ST_DWithin(st_astext(wkb_geometry)::geography,
ST_Point(-73.39993423899995, 43.89050742300003)::geography, 1609.34) limit 1

select ST_X (wkb_geometry) as x, ST_Y (wkb_geometry) as y from powerplants

ALTER TABLE substations
        Add COLUMN x double PRECISION,
        Add COLUMN y double precision;
        
       
update substations
         set x = ST_X (wkb_geometry),
         y = ST_Y (wkb_geometry)
         where ogc_fid  in (select ogc_fid from substations);

## Create Models based on geojson based tables
sqlacodegen postgresql://[user]:[password]@[host]:[port]/[databas] > models.py

## Initial Run
1. `python3 -m venv env`
2. `source env/bin/activate`
3. `python -m pip install --upgrade pip`
4. `pip install -r requirements.txt`

## To run FastAPI based API
python -m uvicorn app.main:app --reload 

## To build docker image

docker build -t geo-utilities-api .

# To run application in docker

docker run -d -p 80:80 geo-utilities-api

# Bundle database and app images and run both as containers

docker compose --file docker-compose.yml up --build -d

# Bring containers down

docker compose down

## Sequence diagram for evstations endpoints

![](GeoDiagram.svg)
<div hidden>
    
    @startuml GeoDiagram

        actor Client
        activate "Utilities API"
        database DB

        autonumber
        Client -> "Utilities API": GET /evstations
        "Utilities API" -> DB: get_evstation_list()
        DB -> "Utilities API": stations
        "Utilities API" -> Client: stations

        autonumber
        Client -> "Utilities API": GET /evstations/id
        "Utilities API" -> DB: get_evstation_detail(id)
        DB -> "Utilities API": station
        "Utilities API" -> Client: station

    @enduml
    
</div>