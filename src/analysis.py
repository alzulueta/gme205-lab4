def total_active_area(parcels):
    total = 0
    for parcel in parcels:
        if parcel.is_active:
            total += parcel.area()
    return total

def parcels_above_threshold(parcels, threshold):
    result = []
    for parcel in parcels:
        if parcel.area() > threshold:
            result.append(parcel.parcel_id)
    return result

def count_by_zone(parcels):
    zone_count = {}
    for parcel in parcels:
        zone_count[parcel.zone] = zone_count.get(parcel.zone, 0) + 1
    return zone_count

def intersecting_parcels(parcels, target_zone):
    # Using zone as proxy for suitability
    result = []
    for parcel in parcels:
        if parcel.zone == target_zone:
            result.append(parcel.parcel_id)
    return result