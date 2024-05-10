ogr2ogr -f PostgreSQL PG:"dbname=platform-api host='localhost' port='4432' user=platform-user password=platform-password" data/EVstations.json -nln evstations

ogr2ogr -f PostgreSQL PG:"dbname=platform-api host='localhost' port='4432' user=platform-user password=platform-password" data/IOUregions.json -nln iouregions

ogr2ogr -f PostgreSQL PG:"dbname=platform-api host='localhost' port='4432' user=platform-user password=platform-password" data/ISORTOregions.json -nln isortoregions

ogr2ogr -f PostgreSQL PG:"dbname=platform-api host='localhost' port='4432' user=platform-user password=platform-password" data/NERCregions.json -nln nercregions

ogr2ogr -f PostgreSQL PG:"dbname=platform-api host='localhost' port='4432' user=platform-user password=platform-password" data/NERCregions.json -nln nercregions

ogr2ogr -f PostgreSQL PG:"dbname=platform-api host='localhost' port='4432' user=platform-user password=platform-password" data/NGLDC.json  -nln nlgdc

ogr2ogr -f PostgreSQL PG:"dbname=platform-api host='localhost' port='4432' user=platform-user password=platform-password" data/Powerlines.json -nln powerlines

ogr2ogr -f PostgreSQL PG:"dbname=platform-api host='localhost' port='4432' user=platform-user password=platform-password" data/PowerPlants.json -nln powerplants

ogr2ogr -f PostgreSQL PG:"dbname=platform-api host='localhost' port='4432' user=platform-user password=platform-password" data/PublicPower.json -nln publicpower

ogr2ogr -f PostgreSQL PG:"dbname=platform-api host='localhost' port='4432' user=platform-user password=platform-password" data/Substations.json -nln substations 
 
