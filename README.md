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
i. Start
ii. Load parcel data from JSON file (parcels.json)
iii. Convert each record into a Parcel object
iv. If no parcels are loaded:
    - Display error message "No parcels found"
    - Stop program
v. Initialize:
    - total_active_area = 0
    - threshold = <user-defined>
    - threshold_list = []
    - zone_count = {}
    - suitable_parcels = []
vi. For each parcel in parcel list:
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
vii. Display results
viii. End