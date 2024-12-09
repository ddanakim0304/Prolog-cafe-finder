from pyswip import Prolog
from generate_list import generate_cafes_prolog_file

# Replace this data with real ones plz!!!
cafe_data = [
    {
        "name": "cafe1",
        "distance": 0.5,
        "price": "$",
        "wifi": "yes",
        "sockets": "yes",
        "vegan": "yes",
        "cash_discount": "no",
        "days_opened": "[monday, tuesday, wednesday, thursday, friday]",
        "open_hour": 9,
        "close_hour": 17
    }
]

# Generate the cafes.pl file
generate_cafes_prolog_file(cafe_data)

# Initialize Prolog interface
prolog = Prolog()
prolog.consult("cafes.pl")

def ask_user():
    """
    Displays a menu to collect user preferences for finding a suitable cafe.
    Validates user inputs for correctness.

    Returns:
        tuple: A tuple containing user inputs:
            - max_distance (float): Maximum distance from residence in kilometers.
            - price (str): Preferred price range ('$'/'$$'/'$$$').
            - wifi (str): Wi-Fi requirement ('yes'/'no').
            - sockets (str): Power socket requirement ('yes'/'no').
            - vegan (str): Dietary requirement for vegan/vegetarian options ('yes'/'no').
            - cash_discount (str): Preference for cafes with cash discounts ('yes'/'no').
            - visit_day (str): Day of the week the user plans to visit.
            - visit_start (int): Arrival time in 24-hour format.
            - visit_end (int): Departure time in 24-hour format.
    """
    print("Welcome to the Cafe Finder Expert System!")
    print("Please answer the following questions to find the best cafe for you 🍵🫖")

    while True:
        try:
            max_distance = float(input("Enter maximum distance from the res (in km): "))
            if max_distance < 0:
                raise ValueError("Distance must be non-negative.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid distance in kilometers.")

    while True:
        price = input("Enter your preferred price range ($, $$, $$$): ").strip()
        if price in ["$", "$$", "$$$"]:
            break
        else:
            print("Invalid input. Please choose from $, $$, or $$$.")

    while True:
        wifi = input("Do you need Wi-Fi? (yes/no): ").strip().lower()
        if wifi in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    while True:
        sockets = input("Do you need power sockets? (yes/no): ").strip().lower()
        if sockets in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    while True:
        vegan = input("Do you need vegan/vegetarian options? (yes/no): ").strip().lower()
        if vegan in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    while True:
        cash_discount = input("Do you prefer cafes with cash discounts? (yes/no): ").strip().lower()
        if cash_discount in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    while True:
        visit_day = input("What day of the week are you visiting? (e.g., monday): ").strip().lower()
        if visit_day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
            break
        else:
            print("Invalid input. Please enter a valid day of the week.")

    while True:
        try:
            visit_start = int(input("Enter your arrival time (24-hour format, e.g., 13 for 1 PM): "))
            if 0 <= visit_start <= 24:
                break
            else:
                raise ValueError("Time must be between 0 and 24.")
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid time in 24-hour format.")

    while True:
        try:
            visit_end = int(input("Enter your departure time (24-hour format, e.g., 15 for 3 PM): "))
            if 0 <= visit_end <= 24 and visit_end >= visit_start:
                break
            else:
                raise ValueError("Time must be between 0 and 24, and later than arrival time.")
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid time in 24-hour format.")

    return max_distance, price, wifi, sockets, vegan, cash_discount, visit_day, visit_start, visit_end


def find_cafe(max_distance, price, wifi, sockets, vegan, cash_discount, visit_day, visit_start, visit_end):
    """
    Queries the Prolog knowledge base to find cafes that match user preferences.

    Args:
        max_distance (float): Maximum distance from residence in kilometers.
        price (str): Preferred price range ('$'/'$$'/'$$$').
        wifi (str): Wi-Fi requirement ('yes'/'no').
        sockets (str): Power socket requirement ('yes'/'no').
        vegan (str): Dietary requirement for vegan/vegetarian options ('yes'/'no').
        cash_discount (str): Preference for cafes with cash discounts ('yes'/'no').
        visit_day (str): Day of the week the user plans to visit.
        visit_start (int): Arrival time in 24-hour format.
        visit_end (int): Departure time in 24-hour format.

    Returns:
        list: A list of dictionaries containing matching cafes from the Prolog query.
    """
    query = (
        f"suitable_cafe(Cafe, {max_distance}, '{price}', {wifi}, {sockets}, {vegan}, "
        f"{cash_discount}, '{visit_day}', {visit_start}, {visit_end})"
    )
    results = list(prolog.query(query))
    return results


def display_results(results):
    """
    Displays the results of the Prolog query.

    Input:
        results (list): A list of dictionaries containing the cafes that match the query.

    Output:
        A list of recommended cafes or a message indicating no matches were found.
    """
    if results:
        print("\n✨ Here are some cafes you might love! ✨")
        for cafe in results:
            print(f"🌟 {cafe['Cafe']}")
    else:
        print("\nNo suitable cafes found based on your preferences :(")


if __name__ == "__main__":
    user_input = ask_user()
    results = find_cafe(*user_input)
    display_results(results)