import json
from spatial import SpatialObject
import analysis

# Load parcels
with open("../data/parcels.json", "r") as f:
    data = json.load(f)

# Convert to SpatialObjects
parcels = []
for d in data:
    parcels.append(SpatialObject(
        parcel_id=d["parcel_id"],
        zone=d["zone"],
        is_active=d["is_active"],
        geometry=d["geometry"]
    ))

# 1. Total active area
total_area = analysis.total_active_area(parcels)
print("Total active area (sqm):", total_area)

# 2. Parcels above threshold
threshold = 500
above_threshold = analysis.parcels_above_threshold(parcels, threshold)
print(f"Parcels above threshold {threshold} sqm:", above_threshold)

# 3. Count by zone
zone_counts = analysis.count_by_zone(parcels)
print("Count by zone:", zone_counts)

# 4. Intersecting parcels (example: Residential)
residential_parcels = analysis.intersecting_parcels(parcels, "Residential")
print("Residential parcels suitable for development:", residential_parcels)