import json
from spatial import Parcel
from analysis import total_active_area, parcels_above_threshold, count_by_zone, intersecting_parcels

# Load parcels from JSON
parcels = []
with open("../data/parcels.json", "r") as f:
    data = json.load(f)

# Create Parcel objects
for d in data:
    parcels.append(Parcel(
        parcel_id=d["parcel_id"],
        zone=d["zone"],
        is_active=d["is_active"],
        geometry=d["geometry"]
    ))

# WGS84 area → approximate sqm conversion
# 1 degree latitude ~ 111,000 m, 1 degree longitude ~ cos(lat) * 111,000 m
def convert_deg2_to_sqm(parcel):
    # Take approximate centroid latitude
    coords = parcel.geometry['coordinates'][0]
    lat = sum([c[1] for c in coords]) / len(coords)
    deg_to_m = 111000
    area_deg2 = parcel.area()  # area in degrees^2
    # Approx conversion using lat for longitude scaling
    return area_deg2 * (deg_to_m ** 2) * abs(round(math.cos(math.radians(lat)), 6))

import math
for p in parcels:
    p.area_sqm = convert_deg2_to_sqm(p)

# 1. Total active area
total_area = total_active_area(parcels)
print(f"Total active area (sqm): {total_area}")

# 2. Parcels above threshold (500 sqm)
threshold = 500
above_thresh = parcels_above_threshold(parcels, threshold)
print(f"Parcels above threshold {threshold} sqm: {above_thresh}")

# 3. Count by zone
zone_counts = count_by_zone(parcels)
print(f"Count by zone: {zone_counts}")

# 4. Parcels suitable for development (e.g., Residential zone)
residential_parcels = intersecting_parcels(parcels, "Residential")
print(f"Residential parcels suitable for development: {residential_parcels}")