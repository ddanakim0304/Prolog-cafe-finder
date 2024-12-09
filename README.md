# Cafe Finder Expert System (CS152 Location-based assignment)

**Cafe Finder Expert System** uses Python and Prolog to recommend cafes based on user preferences. The system collects user inputs such as distance, price range, Wi-Fi availability, power sockets, vegan options, cash discounts, and visiting times, and queries a Prolog knowledge base to find suitable cafes.

## Features
- Collects user preferences through a simple interactive menu.
- Uses Prolog to query a knowledge base of cafes.
- Displays a list of recommended cafes based on user inputs.

## How It Works
1. **Data Generation**:  
   The `generate_cafes_prolog_file` function in `generate_list.py` generates a Prolog file (`cafes.pl`) from the cafe data in `cafe_data.py`.
   
2. **User Input**:  
   The `ask_user` function in `Main.py` collects user preferences.
   
3. **Prolog Query**:  
   The `find_cafe` function in `Main.py` queries the Prolog knowledge base to find cafes that match the user preferences.
   
4. **Display Results**:  
   The `display_results` function in `Main.py` displays the matching cafes.
