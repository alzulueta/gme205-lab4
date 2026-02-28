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

2. Input:
    - parcels_list: list of parcels with attributes
        - parcel_id
        - zone
        - is_active (true/false)
        - area_sqm

3. Initialize:
    - total_area = 0
    - large_parcels_list = empty list
    - zone_counts = empty dictionary
    - development_suitable = empty list
    - threshold_area = 500  # sqm, can be changed
    - proposed_zone = "Residential"  # change depending on development

4. For each parcel in parcels_list:
    a. If parcel.zone not in zone_counts:
        - zone_counts[parcel.zone] = 0
    b. zone_counts[parcel.zone] = zone_counts[parcel.zone] + 1

    c. If parcel.is_active = true:
        - total_area = total_area + parcel.area_sqm
        - If parcel.area_sqm > threshold_area:
            - Add parcel.parcel_id to large_parcels_list

    d. If parcel.zone = proposed_zone:
        - Add parcel.parcel_id to development_suitable

5. Output:
    - "Total area of active parcels: " + total_area
    - "Parcels larger than threshold area: " + large_parcels_list
    - "Number of parcels per zone: " + zone_counts
    - "Parcels suitable for proposed development: " + development_suitable

6. End

# Pseudocode 
START

INPUT parcels_list
SET total_area = 0
SET large_parcels_list = empty list
SET zone_counts = empty dictionary
SET development_suitable = empty list
SET threshold_area = 500   
SET proposed_zone = "Residential" 

FOR EACH parcel IN parcels_list
    IF parcel.zone NOT IN zone_counts THEN
        zone_counts[parcel.zone] = 0
    END IF
    zone_counts[parcel.zone] = zone_counts[parcel.zone] + 1
    
    IF parcel.is_active = true THEN
        total_area = total_area + parcel.area_sqm
        
        IF parcel.area_sqm > threshold_area THEN
            ADD parcel.parcel_id TO large_parcels_list
        END IF
    END IF
    
    IF parcel.zone = proposed_zone THEN
        ADD parcel.parcel_id TO development_suitable
    END IF
END FOR

OUTPUT "Total area of active parcels:", total_area
OUTPUT "Parcels larger than threshold area:", large_parcels_list
OUTPUT "Number of parcels per zone:", zone_counts
OUTPUT "Parcels suitable for proposed development:", development_suitable

END

## Reflection

1. Sequence: Appears in the step-by-step operations in analysis.py, e.g., reading data, filtering, and computing metrics in order.

Selection: Implemented using if/elif/else statements to apply different rules or conditions on parcels.

Repetition: Appears in loops, such as iterating over parcels to apply analysis functions or filters.

2. The code would likely become less organized and harder to debug. Logic may be scattered across classes, and dependencies between steps may be unclear, making future modifications error-prone.

3. Spatial behavior is encapsulated in methods of spatial objects (e.g., Parcel class) and in analysis.py functions that operate on these objects. This separation ensures that objects manage their own spatial data, while analysis modules handle broader operations, improving modularity and maintainability.

4. analysis.py contains the core algorithms and structured workflows because it defines how data is processed and analyzed while demo.py only demonstrates usage, keeping presentation separate from logic, which simplifies testing and reuse.

5. The Parcel class could become a “God class”, taking on too many responsibilities (data storage + analysis) which makes the system harder to maintain, extend, or test, and tightly couples object behavior with all filtering rules.

6. With structured logic in analysis.py, adding a new rule is straightforward: modify or add a function without changing the Parcel class. This demonstrates the flexibility and extensibility of separating analysis from object behavior.

7. By keeping objects responsible only for their data and core behaviors and placing broader workflow logic elsewhere, no single class becomes overloaded. This improves modularity, testability, and code clarity, avoiding a central class that does everything.