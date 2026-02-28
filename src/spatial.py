class SpatialObject:
    def __init__(self, geometry):
        self.geometry = geometry  # expects a dict like GeoJSON polygon
    def area(self):
        """
        Approximate conversion from WGS84 degrees to square meters.
        Uses a simple formula assuming small areas near the equator:
        1 deg latitude ~ 111320 meters
        1 deg longitude ~ 111320 * cos(lat) meters
        """
        coords = self.geometry.get("coordinates", [[]])[0]
        if not coords:
            return 0
        # approximate using bounding box
        lats = [pt[1] for pt in coords]
        lons = [pt[0] for pt in coords]
        lat_min, lat_max = min(lats), max(lats)
        lon_min, lon_max = min(lons), max(lons)
        # center latitude for longitude scaling
        lat_center = sum(lats)/len(lats)
        meter_per_deg_lat = 111320
        meter_per_deg_lon = 111320 * abs(math.cos(math.radians(lat_center)))
        width_m = (lon_max - lon_min) * meter_per_deg_lon
        height_m = (lat_max - lat_min) * meter_per_deg_lat
        return abs(width_m * height_m)
import math
class Parcel(SpatialObject):
    def __init__(self, parcel_id, zone, is_active, geometry):
        super().__init__(geometry)
        self.parcel_id = parcel_id
        self.zone = zone
        self.is_active = is_active