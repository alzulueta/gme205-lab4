def total_active_area(parcels):
    """Return total area (sqm) of active parcels."""
    total = 0
    for parcel in parcels:  # repetition
        if parcel.is_active:  # conditional
            total += parcel.area()
    return total
def parcels_above_threshold(parcels, threshold):
    """Return list of parcel IDs above threshold area (sqm)."""
    result = []
    for parcel in parcels:
        if parcel.area() > threshold:
            result.append(parcel.parcel_id)
    return result
def count_by_zone(parcels):
    """Return dictionary of counts by zone."""
    zone_counts = {}
    for parcel in parcels:
        zone = parcel.zone
        if zone in zone_counts:
            zone_counts[zone] += 1
        else:
            zone_counts[zone] = 1
    return zone_counts
def intersecting_parcels(parcels, zone_name):
    """Return parcel IDs that are in the specified zone (example: Residential)."""
    result = []
    for parcel in parcels:
        if parcel.zone == zone_name:
            result.append(parcel.parcel_id)
    return result