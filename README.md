# Cafe Finder Expert System (CS152 Location-based assignment)

**Cafe Finder Expert System** uses Python and Prolog to recommend cafes based on user preferences. The system collects user inputs such as distance, price range, Wi-Fi availability, power sockets, vegan options, meals, and visiting times, and queries a Prolog knowledge base to find suitable cafes.


## Algorithm Visualization
```mermaid
flowchart TD
    A[Collect User Preferences] --> B[Check Preferred Transport and Max Transport Time]
    B --> |User Input = Taxi or Public Transport| B1[Check if the cafe is within walkable distance]
    B1 --> |If Walktime <= 10| C
    B1 --> |If Walktime > 10| B3[Selected Transport Time <= Max Transport Time]
    B3 --> |Pass| C
    B3 --> |Fail| Z
    B --> |User Input = Walk| B2[Walk Time <= Max Transport Time]
    B2 --> C
    
    C[Check WiFi Requirement]
    C -->|User Input = no| D[Check Socket Requirement]
    C -->|User Input = yes| C2[Verify Wifi = yes]
    C2 -->|Pass| D
    C2 -->|Fail| Z[Reject Cafe]

    %% Socket Check
    D -->|User Input = no| G[Check Dietary Preferences]
    D -->|User Input = yes| E2[Verify Socket = yes]
    E2 -->|Pass| G
    E2 -->|Fail| Z

    %% Dietary Check
    G -->|User Input = none| H[Check Meals Requirement]
    G -->|User Input = vegan| G2[Verify vegan options include vegan]
    G -->|User Input = vegetarian| G3[Verify vegan options include vegetarian]
    G2 -->|Pass| H
    G2 -->|Fail| Z
    G3 -->|Pass| H
    G3 -->|Fail| Z

    %% Meals Requirement
    H -->|User Input = no| J[Check Day and Time Availability]
    H -->|User Input = yes| I2[Verify meals = yes]
    I2 -->|Pass| J
    I2 -->|Fail| Z

    %% Time Availability
    J --> K1[Verify VisitDay]
    K1 -->|Pass| K2[Check Open and Close Hours]
    K2 -->|Pass| L[Add to result]
    K2 -->|Fail| Z
    K1 -->|Fail| Z
```


## Features
- Collects user preferences through a simple interactive menu.
- Uses Prolog to query a knowledge base of cafes.
- Displays a list of recommended cafes based on user inputs.

## How It Works
1. **Data Generation**:  
   The `generate_cafes_prolog_file` function in [`generate_list.py`](generate_list.py) generates a Prolog file (`cafes.pl`) from the cafe data in [`cafe_data.py`](cafe_data.py). This function processes the cafe data and writes Prolog facts for each cafe, including details such as address, travel times, price range, Wi-Fi availability, power sockets, vegan/vegetarian options, meals, days opened, and opening/closing hours.

2. **User Input**:  
   The `ask_user` function in [`main.py`](main.py) collects user preferences through an interactive menu. It validates user inputs for correctness and returns a tuple containing the user inputs:
   - `transport` (str): Preferred mode of transport ('walk', 'public_transport', 'taxi').
   - `max_time` (int): Maximum travel time in minutes.
   - `max_price` (int): Maximum price in peso.
   - `wifi` (str): Wi-Fi requirement ('yes'/'no').
   - `sockets` (str): Power socket requirement ('yes'/'no').
   - `vegan_preference` (str): Dietary requirement ('vegan'/'vegetarian'/'none').
   - `needs_meals` (str): Preference for cafes that serve meals ('yes'/'no').
   - `visit_day` (str): Day of the week the user plans to visit.
   - `visit_start` (int): Arrival time in 24-hour format.
   - `visit_end` (int): Departure time in 24-hour format.

3. **Prolog Query**:  
   The `find_cafe` function in [`main.py`](main.py) queries the Prolog knowledge base to find cafes that match the user preferences. It constructs a Prolog query using the user inputs and retrieves matching cafes. The function also retrieves the addresses for each cafe found and combines the results.

4. **Display Results**:  
   The `display_results` function in [`main.py`](main.py) displays the matching cafes in a natural language format with a numbered list. It shows the name, address, and travel time for each cafe based on the user's preferred mode of transport. If no suitable cafes are found, it displays a message indicating that no matches were found.
