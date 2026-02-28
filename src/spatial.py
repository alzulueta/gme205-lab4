import math

class SpatialObject:
    def __init__(self, parcel_id, zone, is_active, geometry):
        self.parcel_id = parcel_id
        self.zone = zone
        self.is_active = is_active
        self.geometry = geometry  # GeoJSON-like polygon

    def area(self):
        """
        Returns approximate area in square meters (sqm) from WGS84 coordinates.
        """
        deg_area = self._geometry_area_degrees()
        centroid_lat = self._centroid_lat()
        meters_per_deg = 111320  # 1° ≈ 111.32 km
        sqm_area = deg_area * (meters_per_deg**2) * math.cos(math.radians(centroid_lat))
        return sqm_area

    def _geometry_area_degrees(self):
        """
        Compute polygon area in degrees using the shoelace formula.
        """
        coords = self.geometry['coordinates'][0]
        n = len(coords)
        area = 0
        for i in range(n):
            x0, y0 = coords[i]
            x1, y1 = coords[(i + 1) % n]
            area += x0 * y1 - x1 * y0
        return abs(area) / 2

    def _centroid_lat(self):
        """
        Compute approximate latitude of polygon centroid.
        """
        coords = self.geometry['coordinates'][0]
        y_coords = [y for x, y in coords]
        return sum(y_coords) / len(y_coords)