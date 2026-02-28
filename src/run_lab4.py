import json
import os
from spatial import Parcel
import analysis

# --- 1. Load JSON file ---
def load_parcels(json_path):
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found!")
        return None
    with open(json_path, "r") as f:
        return json.load(f)

# --- 2. Construct Parcel objects ---
def construct_parcel_objects(parcel_data):
    parcels = []
    for d in parcel_data:
        parcels.append(Parcel(
            parcel_id=d["parcel_id"],
            zone=d["zone"],
            is_active=d["is_active"],
            geometry=d["geometry"]
        ))
    return parcels

# --- 3. Save summary to JSON ---
def save_summary(summary, output_path="output/summary.json"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(summary, f, indent=4)
    print(f"Summary saved to {output_path}")

# --- 4. Main structured flow ---
def main():
    # Load data
    parcel_data = load_parcels("../data/parcels.json")
    if parcel_data is None or len(parcel_data) == 0:
        print("No parcels loaded. Exiting.")
        return

    # Create objects
    parcels = construct_parcel_objects(parcel_data)

    # Analysis computations
    total_area = analysis.total_active_area(parcels)
    threshold = 500  # sqm
    parcels_over_threshold = analysis.parcels_above_threshold(parcels, threshold)
    count_zone = analysis.count_by_zone(parcels)
    # Example: Residential parcels suitable for development
    residential_parcels = analysis.intersecting_parcels(parcels, "Residential")

    # Print results
    print(f"Total active area (sqm): {total_area}")
    print(f"Parcels above threshold {threshold} sqm: {parcels_over_threshold}")
    print(f"Count by zone: {count_zone}")
    print(f"Residential parcels suitable for development: {residential_parcels}")

    # Save summary
    summary = {
        "total_active_area_sqm": total_area,
        "parcels_above_threshold_sqm": parcels_over_threshold,
        "count_by_zone": count_zone,
        "residential_parcels_suitable": residential_parcels
    }
    save_summary(summary)

if __name__ == "__main__":
    main()