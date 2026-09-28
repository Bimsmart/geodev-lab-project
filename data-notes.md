# Data notes
## GRID3 Nigeria Operational LGA v3.0
- Source: https://data.grid3.org
- Downloaded: 
- 774 features, polygons
- Columns:  lga_name (text), statecode (text), statename (text), statecode (text) 
- No nulls in lga_name
- Covers my LGA fully

## GRID3 Nigeria Operational Wards v3.0
- Source: https://data.grid3.org
- Downloaded: 
- 377 features, polygons
- Columns:  ward_name (text), statename (text), lganame, lgacode, wardcode,
- No nulls in ward.
- Covers my LGA fully
- Extracted: clipped area of interest.
- 36 wards, polygons in Alimosho LGA.
  
## OSM roads, 
- Source: https://download.geofabrik.de
- Extracted: clipped area of interest 
- 12,796 features, lines
- most names are NULL.
- Coverage looks good.

  
#CRS and preparation
## CRS and preparation
- All source layers arrived in EPSG:4326
- Study area: Alimosho LGA, extracted from GRID3 wards
- All layers (roads and wards) clipped to study area, then reprojected to EPSG:32631 (UTM 31N) 
- Area check: Alimosho LGA 182.827863997222 km2, matches published figure


## OSM roads, Alimosho
- Extracted
- 12796 features
- COMPLETENESS: good in built-up area. Compared my own street: All roads present. 
- CURRENCY: my street is up to date
- POSITIONAL: roads aligned well with satellite imagery, no systematic offset visible.
- ATTRIBUTE: majority of the roads do not have names, not recorded.
- FITNESS: adequate 

