# Data notes
## GRID3 Nigeria Operational LGA v3.0
- Source: https://data.grid3.org
- Downloaded: 
- 774 features, polygons
- Columns:  lga_name (text), state (text)
- No nulls in lga_name
- Covers my LGA fully
## OSM roads, geofabrik.de
- Extracted: clipped area of interest 
- 12,796 features, lines
- most names are NULL.
- Coverage looks good.

  
#CRS and preparation
## CRS and preparation
- All source layers arrived in EPSG:4326
- Study area: Alimosho LGA, extracted from GRID3 wards
- All layers clipped to study area, then reprojected to EPSG:32631 (UTM 31N)
- Area check: Alimosho LGA 182.827863997222 m2, matches published figure
- Working files in data/processed/, raw files untouched

