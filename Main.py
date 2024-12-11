from pyswip import Prolog
from generate_list import generate_cafes_prolog_file
from cafe_data import cafe_data

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
            - transport (str): Preferred mode of transport ('walk', 'public_transport', 'taxi').
            - max_time (int): Maximum travel time in minutes.
            - max_price (int): Maximum price in peso.
            - wifi (str): Wi-Fi requirement ('yes'/'no').
            - sockets (str): Power socket requirement ('yes'/'no').
            - vegan_preference (str): Dietary requirement ('vegan'/'vegetarian'/'none').
            - needs_meals (str): Preference for cafes that serve meals ('yes'/'no').
            - visit_day (str): Day of the week the user plans to visit.
            - visit_start (int): Arrival time in 24-hour format.
            - visit_end (int): Departure time in 24-hour format.
    """
    print("Welcome to the Cafe Finder Expert System!")
    print("Please answer the following questions to find the best cafe for you 🍵🫖")

    while True:
        try:
            transport = input("What transportation do you prefer? (walk/public_transport/taxi): ").strip().lower()
            if transport not in ["walk", "public_transport", "taxi"]:
                raise ValueError("Invalid transport option. Choose 'walk', 'public_transport', or 'taxi'.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    while True:
        try:
            max_time = int(input(f"What is the maximum travel time by {transport} (in minutes)? "))
            if max_time < 0:
                raise ValueError("Time must be non-negative.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    while True:
        try:
            max_price = int(input("Enter your maximum price (in Argentinian Peso): "))
            if max_price < 0:
                raise ValueError("Price must be non-negative.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

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
        vegan_preference = input("Do you have dietary preferences? (vegan/vegetarian/none): ").strip().lower()
        if vegan_preference in ["vegan", "vegetarian", "none"]:
            break
        else:
            print("Invalid input. Please choose 'vegan', 'vegetarian', or 'none'.")

    while True:
        needs_meals = input("Do you require meals at the cafe? (yes/no): ").strip().lower()
        if needs_meals in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    while True:
        visit_day = input("What day of the week are you visiting? (ex. monday): ").strip().lower()
        if visit_day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
            break
        else:
            print("Invalid input. Please enter a valid day of the week.")

    while True:
        try:
            visit_start = int(input("Enter your arrival time (24-hour format, ex. 13 for 1 PM): "))
            if 0 <= visit_start <= 24:
                break
            else:
                raise ValueError("Time must be between 0 and 24.")
        except ValueError as e:
            print(f"Invalid input: {e}")

    while True:
        try:
            visit_end = input("Enter your departure time (24-hour format, ex. 15 for 3 PM, or 26 for 2 AM the next day): ").strip()
            if visit_end.isdigit():
                visit_end = int(visit_end)
                if 0 <= visit_end <= 48:  # Allow times up to 48 (24+24 hours)
                    if visit_end <= 24 or visit_end >= visit_start:
                        break
                    else:
                        raise ValueError("Departure time must be later than arrival time.")
                else:
                    raise ValueError("Time must be between 0 and 48 (24+next day).")
            else:
                raise ValueError("Please enter a valid integer for the time.")
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid time.")

    return transport, max_time, max_price, wifi, sockets, vegan_preference, needs_meals, visit_day, visit_start, visit_end


def find_cafe(transport, max_time, max_price, wifi, sockets, vegan_preference, needs_meals, visit_day, visit_start, visit_end):
    """
    Queries the Prolog knowledge base to find cafes that match user preferences.

    Args:
        transport (str): Preferred mode of transport ('walk', 'public_transport', 'taxi').
        max_time (int): Maximum travel time in minutes.
        max_price (int): Maximum price in local currency.
        wifi (str): Wi-Fi requirement ('yes'/'no').
        sockets (str): Power socket requirement ('yes'/'no').
        vegan_preference (str): Dietary requirement ('vegan'/'vegetarian'/'none').
        needs_meals (str): Preference for cafes that serve meals ('yes'/'no').
        visit_day (str): Day of the week the user plans to visit.
        visit_start (int): Arrival time in 24-hour format.
        visit_end (int): Departure time in 24-hour format.

    Returns:
        list: A list of dictionaries containing matching cafes from the Prolog query.
    """
    try:
        query = (
            f"suitable_cafe(Cafe, '{transport}', {max_time}, {max_price}, {wifi}, {sockets}, "
            f"'{vegan_preference}', {needs_meals}, '{visit_day}', {visit_start}, {visit_end})"
        )
        results = list(prolog.query(query))
        return results
    except Exception as e:
        print(f"Error querying Prolog: {e}")
        return []


def display_results(results):
    """
    Displays the results of the Prolog query.

    Args:
        results (list): A list of dictionaries containing the cafes that match the query.

    Output:
        Prints a list of recommended cafes or a message indicating no matches were found.
    """
    if results:
        print("\n✨ Here are some cafes you might love! ✨")
        for cafe in results:
            print(f"🌟 {cafe['Cafe'].replace('_', ' ')}")
    else:
        print("\nNo suitable cafes found based on your preferences :(")


if __name__ == "__main__":
    try:
        user_input = ask_user()
        results = find_cafe(*user_input)
        display_results(results)
    except Exception as e:
        print(f"An error occurred: {e}")
