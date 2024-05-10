from datetime import datetime
from pydantic import BaseModel


class SubStationResponse(BaseModel):
    """Response for SubStations"""

    ogc_fid: int
    objectid: int
    msid: str
    subname: str
    subtype: str
    primvolt: int
    secvolt: int
    tertvolt: int
    capacity: int
    transerv: int
    status: str
    owner: str
    ownerid: str
    numowners: str
    operator: str
    operatorid: str
    numopers: str
    leased: str
    projectid: str
    projectname: str
    install_dt: int
    routetype: str
    updated: datetime
    updt_sp: datetime
    img_source: str
    resolution: str
    metacode: str
    map_id: str
    mapscale: str
    lastowner: str
    lastownid: str
    lastoper: str
    lastoperid: str
    release_dt: datetime
    source: str
    expiration: str
    # wkb_geometry: #
