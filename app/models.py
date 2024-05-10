# coding: utf-8
from sqlalchemy import (
    BigInteger,
    CheckConstraint,
    Column,
    Float,
    Integer,
    String,
    Table,
    Text,
    text,
)
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Evstation(Base):
    __tablename__ = "evstations"

    ogc_fid = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('evstations_ogc_fid_seq'::regclass)"),
    )
    objectid = Column(Integer)
    msid = Column(String)
    name = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    zip = Column(String)
    country = Column(String)
    status = Column(String)
    private = Column(String)
    accesstime = Column(String)
    inst_yr = Column(String)
    connecttyp = Column(String)
    lvl1_count = Column(String)
    lvl2_count = Column(String)
    dc_count = Column(String)
    other = Column(String)
    network = Column(String)
    updated = Column(String)
    updt_sp = Column(BigInteger)
    metacode = Column(String)
    release_dt = Column(BigInteger)
    source = Column(String)
    expiration = Column(String)
    wkb_geometry = Column(NullType, index=True)
    x = Column(NullType, index=True)
    y = Column(NullType, index=True)


t_geography_columns = Table(
    "geography_columns",
    metadata,
    Column("f_table_catalog", String),
    Column("f_table_schema", String),
    Column("f_table_name", String),
    Column("f_geography_column", String),
    Column("coord_dimension", Integer),
    Column("srid", Integer),
    Column("type", Text),
)


t_geometry_columns = Table(
    "geometry_columns",
    metadata,
    Column("f_table_catalog", String(256)),
    Column("f_table_schema", String),
    Column("f_table_name", String),
    Column("f_geometry_column", String),
    Column("coord_dimension", Integer),
    Column("srid", Integer),
    Column("type", String(30)),
)


class Iouregion(Base):
    __tablename__ = "iouregions"

    ogc_fid = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('iouregions_ogc_fid_seq'::regclass)"),
    )
    objectid = Column(Integer)
    owner = Column(String)
    ownerid = Column(String)
    operator = Column(String)
    operatorid = Column(String)
    eia_util = Column(Integer)
    lastowner = Column(String)
    lastownid = Column(String)
    lastoper = Column(String)
    lastoperid = Column(String)
    updated = Column(BigInteger)
    updt_sp = Column(BigInteger)
    metacode = Column(String)
    map_id = Column(String)
    mapscale = Column(String)
    release_dt = Column(BigInteger)
    source = Column(String)
    expiration = Column(String)
    shape_length = Column(Float(53))
    shape_area = Column(Float(53))
    wkb_geometry = Column(NullType, index=True)


class Isortoregion(Base):
    __tablename__ = "isortoregions"

    ogc_fid = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('isortoregions_ogc_fid_seq'::regclass)"),
    )
    objectid = Column(Integer)
    name = Column(String)
    pop_name = Column(String)
    map_id = Column(String)
    metacode = Column(String)
    mapscale = Column(String)
    updated = Column(BigInteger)
    updt_sp = Column(BigInteger)
    release_dt = Column(BigInteger)
    source = Column(String)
    expiration = Column(String)
    shape_length = Column(Float(53))
    shape_area = Column(Float(53))
    wkb_geometry = Column(NullType, index=True)


class Nercregion(Base):
    __tablename__ = "nercregions"

    ogc_fid = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('nercregions_ogc_fid_seq'::regclass)"),
    )
    objectid = Column(Integer)
    region = Column(String)
    pop_name = Column(String)
    coregion = Column(String)
    copop_name = Column(String)
    updated = Column(BigInteger)
    updt_sp = Column(BigInteger)
    metacode = Column(String)
    map_id = Column(String)
    release_dt = Column(BigInteger)
    source = Column(String)
    expiration = Column(String)
    shape_length = Column(Float(53))
    shape_area = Column(Float(53))
    wkb_geometry = Column(NullType, index=True)


class Nlgdc(Base):
    __tablename__ = "nlgdc"

    ogc_fid = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('nlgdc_ogc_fid_seq'::regclass)"),
    )
    objectid = Column(Integer)
    owner = Column(String)
    ownerid = Column(String)
    operator = Column(String)
    operatorid = Column(String)
    eia_util = Column(Integer)
    lastowner = Column(String)
    lastownid = Column(String)
    lastoper = Column(String)
    lastoperid = Column(String)
    updated = Column(BigInteger)
    updt_sp = Column(BigInteger)
    metacode = Column(String)
    map_id = Column(String)
    mapscale = Column(String)
    release_dt = Column(BigInteger)
    source = Column(String)
    expiration = Column(String)
    shape_length = Column(Float(53))
    shape_area = Column(Float(53))
    wkb_geometry = Column(NullType, index=True)


class Powerline(Base):
    __tablename__ = "powerlines"

    ogc_fid = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('powerlines_ogc_fid_seq'::regclass)"),
    )
    objectid = Column(Integer)
    msid = Column(String)
    voltage = Column(Float(53))
    range = Column(String)
    hivoltage = Column(Integer)
    volt_cat = Column(String)
    type = Column(String)
    status = Column(String)
    corridor = Column(String)
    owner = Column(String)
    ownerid = Column(String)
    numowners = Column(String)
    operator = Column(String)
    operatorid = Column(String)
    projectid = Column(String)
    projectname = Column(String)
    install_dt = Column(Integer)
    routetype = Column(String)
    linename = Column(String)
    updated = Column(BigInteger)
    updt_sp = Column(BigInteger)
    img_source = Column(String)
    resolution = Column(String)
    metacode = Column(String)
    map_id = Column(String)
    mapscale = Column(String)
    lastowner = Column(String)
    lastownid = Column(String)
    lastoper = Column(String)
    lastoperid = Column(String)
    mileage = Column(Float(53))
    release_dt = Column(BigInteger)
    source = Column(String)
    expiration = Column(String)
    shape_length = Column(Float(53))
    wkb_geometry = Column(NullType, index=True)


class Powerplant(Base):
    __tablename__ = "powerplants"

    ogc_fid = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('powerplants_ogc_fid_seq'::regclass)"),
    )
    objectid = Column(Integer)
    msid = Column(String)
    facname = Column(String)
    owner = Column(String)
    ownerid = Column(String)
    numowners = Column(String)
    operator = Column(String)
    operatorid = Column(String)
    numopers = Column(String)
    leased = Column(String)
    yrinstall = Column(Integer)
    name_cap = Column(Float(53))
    numunits = Column(Integer)
    prop_cap = Column(Float(53))
    propunit = Column(Integer)
    status = Column(String)
    non_util = Column(String)
    nuclear = Column(String)
    fossilfuel = Column(String)
    renewable = Column(String)
    primefuel = Column(String)
    primemover = Column(String)
    reservoir = Column(String)
    river = Column(String)
    eia_cd = Column(String)
    updated = Column(BigInteger)
    updt_sp = Column(BigInteger)
    img_source = Column(String)
    resolution = Column(String)
    metacode = Column(String)
    map_id = Column(String)
    mapscale = Column(String)
    lastowner = Column(String)
    lastownid = Column(String)
    lastoper = Column(String)
    lastoperid = Column(String)
    release_dt = Column(BigInteger)
    source = Column(String)
    expiration = Column(String)
    wkb_geometry = Column(NullType, index=True)


class Publicpower(Base):
    __tablename__ = "publicpower"

    ogc_fid = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('publicpower_ogc_fid_seq'::regclass)"),
    )
    objectid = Column(Integer)
    companytype = Column(String)
    owner = Column(String)
    ownerid = Column(String)
    operator = Column(String)
    operatorid = Column(String)
    eia_utility = Column(Integer)
    lastowner = Column(String)
    lastownid = Column(String)
    lastoper = Column(String)
    lastoperid = Column(String)
    gtentity = Column(String)
    gtentid = Column(String)
    gtentfed = Column(String)
    gtentfedid = Column(String)
    cao = Column(String)
    cao_id = Column(String)
    operatorstate = Column(String)
    nercregion = Column(String)
    updated = Column(BigInteger)
    updt_sp = Column(BigInteger)
    metacode = Column(String)
    map_id = Column(String)
    mapscale = Column(String)
    release_dt = Column(BigInteger)
    source = Column(String)
    expiration = Column(String)
    shape_length = Column(Float(53))
    shape_area = Column(Float(53))
    wkb_geometry = Column(NullType, index=True)


class SpatialRefSy(Base):
    __tablename__ = "spatial_ref_sys"
    __table_args__ = (CheckConstraint("(srid > 0) AND (srid <= 998999)"),)

    srid = Column(Integer, primary_key=True)
    auth_name = Column(String(256))
    auth_srid = Column(Integer)
    srtext = Column(String(2048))
    proj4text = Column(String(2048))


class Substation(Base):
    __tablename__ = "substations"

    ogc_fid = Column(
        Integer,
        primary_key=True,
        server_default=text("nextval('substations_ogc_fid_seq'::regclass)"),
    )
    objectid = Column(Integer)
    msid = Column(String)
    subname = Column(String)
    subtype = Column(String)
    primvolt = Column(Integer)
    secvolt = Column(Integer)
    tertvolt = Column(Integer)
    capacity = Column(Integer)
    transerv = Column(Integer)
    status = Column(String)
    owner = Column(String)
    ownerid = Column(String)
    numowners = Column(String)
    operator = Column(String)
    operatorid = Column(String)
    numopers = Column(String)
    leased = Column(String)
    projectid = Column(String)
    projectname = Column(String)
    install_dt = Column(Integer)
    routetype = Column(String)
    updated = Column(BigInteger)
    updt_sp = Column(BigInteger)
    img_source = Column(String)
    resolution = Column(String)
    metacode = Column(String)
    map_id = Column(String)
    mapscale = Column(String)
    lastowner = Column(String)
    lastownid = Column(String)
    lastoper = Column(String)
    lastoperid = Column(String)
    release_dt = Column(BigInteger)
    source = Column(String)
    expiration = Column(String)
    x = Column(NullType, index=True)
    y = Column(NullType, index=True)
