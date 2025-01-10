ogr2ogr -f PostgreSQL PG:"dbname=postgres host='localhost' port='5432' user=postgres password=mypassword" data/mapsearch/EVstations.json -nln evstations

ogr2ogr -f PostgreSQL PG:"dbname=postgres host='localhost' port='5432' user=postgres password=mypassword" data/mapsearch/IOUregions.json -nln iouregions

ogr2ogr -f PostgreSQL PG:"dbname=postgres host='localhost' port='5432' user=postgres password=mypassword" data/mapsearch/ISORTOregions.json -nln isortoregions

ogr2ogr -f PostgreSQL PG:"dbname=postgres host='localhost' port='5432' user=postgres password=mypassword" data/mapsearch/NERCregions.json -nln nercregions

ogr2ogr -f PostgreSQL PG:"dbname=postgres host='localhost' port='5432' user=postgres password=mypassword" data/mapsearch/NERCregions.json -nln nercregions

ogr2ogr -f PostgreSQL PG:"dbname=postgres host='localhost' port='5432' user=postgres password=mypassword" data/mapsearch/NGLDC.json  -nln nlgdc

ogr2ogr -f PostgreSQL PG:"dbname=postgres host='localhost' port='5432' user=postgres password=mypassword" data/mapsearch/Powerlines.json -nln powerlines

ogr2ogr -f PostgreSQL PG:"dbname=postgres host='localhost' port='5432' user=postgres password=mypassword" data/mapsearch/PowerPlants.json -nln powerplants

ogr2ogr -f PostgreSQL PG:"dbname=postgres host='localhost' port='5432' user=postgres password=mypassword" data/mapsearch/PublicPower.json -nln publicpower

ogr2ogr -f PostgreSQL PG:"dbname=postgres host='localhost' port='5432' user=postgres password=mypassword" data/mapsearch/Substations.json -nln substations 
 
