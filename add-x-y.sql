ALTER TABLE evstations
        Add COLUMN x double PRECISION,
        Add COLUMN y double precision;
        
       
update evstations
         set x = ST_X (wkb_geometry),
         y = ST_Y (wkb_geometry)
         where ogc_fid  in (select ogc_fid from evstations);

ALTER TABLE substations
        Add COLUMN x double PRECISION,
        Add COLUMN y double precision;
        
       
update substations
         set x = ST_X (wkb_geometry),
         y = ST_Y (wkb_geometry)
         where ogc_fid  in (select ogc_fid from substations);

ALTER TABLE powerlines
        Add COLUMN x double PRECISION,
        Add COLUMN y double precision;
        
       
update powerlines
         set x = ST_X (wkb_geometry),
         y = ST_Y (wkb_geometry)
         where ogc_fid  in (select ogc_fid from powerlines);

ALTER TABLE powerplants
        Add COLUMN x double PRECISION,
        Add COLUMN y double precision;
        
       
update powerplants
         set x = ST_X (wkb_geometry),
         y = ST_Y (wkb_geometry)
         where ogc_fid  in (select ogc_fid from powerplants);

