# GmE 205 Lab 4 Structured Programming + Object Systems Integration
# How to set up the virtual environment
1. Open the VS Code Terminal
2. Create the virtual environment: python3 -m venv .venv
3. Activate the environment: source .venv/bin/activate
4. Install packages: pip install pandas matplotlib shapely
5. Saved installed packages: pip freeze > requirements.txt
# How to run Python scripts
Make sure the virtual environment is activated ((.venv) shows in the terminal)

# Algorithm
1. Start
2. Load parcel data from JSON file (parcels.json)
3. Convert each record into a Parcel object
4. If no parcels are loaded:
    - Display error message "No parcels found"
    - Stop program
5. Initialize:
    - total_active_area = 0
    - threshold = <user-defined>
    - threshold_list = []
    - zone_count = {}
    - suitable_parcels = []
6. For each parcel in parcel list:
    - If parcel is active:
        Add its area to total_active_area
    - If parcel area exceeds threshold:
        Add parcel to threshold_list
    - Update zone_count:
        If parcel.zone exists in zone_count:
            Increment count
        Else:
            Initialize count = 1
    - If parcel is Residential or Commercial:
        Add parcel to suitable_parcels
7. Display results
8. End

# Pseudocode 
BEGIN

LOAD parcel_data from JSON file
CONVERT parcel_data into Parcel objects
STORE in parcel_list

IF parcel_list is empty THEN
    PRINT "No parcels found."
    STOP
END IF

SET total_active_area = 0
SET threshold = <user-defined value>
INITIALIZE threshold_list = []
INITIALIZE zone_count = {}
INITIALIZE suitable_parcels = []

FOR EACH parcel IN parcel_list DO

    IF parcel.is_active THEN
        total_active_area = total_active_area + parcel.area_sqm
    END IF

    IF parcel.area_sqm > threshold THEN
        ADD parcel TO threshold_list
    END IF

    IF parcel.zone IN zone_count THEN
        zone_count[parcel.zone] = zone_count[parcel.zone] + 1
    ELSE
        zone_count[parcel.zone] = 1
    END IF

    IF parcel.zone == "Residential" OR parcel.zone == "Commercial" THEN
        ADD parcel TO suitable_parcels
    END IF

END FOR

PRINT "Total active area: ", total_active_area
PRINT "Parcels above threshold: ", threshold_list
PRINT "Parcels per zone: ", zone_count
PRINT "Parcels suitable for development: ", suitable_parcels

END