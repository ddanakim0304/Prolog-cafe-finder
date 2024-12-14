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
    print("Please answer the following questions to find the best cafe for you 🍵🫖\n")

    user_transport_labels = ["Walk", "Public Transport", "Taxi/Moto"]
    transport_options = ["walk", "public_transport", "taxi"]

    print("What transportation do you prefer?")
    for i, option in enumerate(user_transport_labels, 1):
        print(f"{i}. {option}")
    while True:
        try:
            transport_choice = int(input("Choose an option (1/2/3): ")) - 1
            transport = transport_options[transport_choice]
            break
        except (ValueError, IndexError):
            print("Invalid input. Please enter 1, 2, or 3.")

    while True:
        try:
            max_time = int(
                input(
                    f"What is the maximum travel time by {user_transport_labels[transport_choice]} (in minutes)? "
                )
            )
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

    wifi_options = ["yes", "no"]
    print("Do you need Wi-Fi?")
    for i, option in enumerate(wifi_options, 1):
        print(f"{i}. {option.capitalize()}")
    while True:
        try:
            wifi_choice = int(input("Choose an option (1/2): ")) - 1
            wifi = wifi_options[wifi_choice]
            break
        except (ValueError, IndexError):
            print("Invalid input. Please enter 1 or 2.")

    print("Do you need power sockets?")
    for i, option in enumerate(wifi_options, 1):
        print(f"{i}. {option.capitalize()}")
    while True:
        try:
            sockets_choice = int(input("Choose an option (1/2): ")) - 1
            sockets = wifi_options[sockets_choice]
            break
        except (ValueError, IndexError):
            print("Invalid input. Please enter 1 or 2.")

    vegan_options = ["vegan", "vegetarian", "none"]
    print("Do you have dietary preferences?")
    for i, option in enumerate(vegan_options, 1):
        print(f"{i}. {option.capitalize()}")
    while True:
        try:
            vegan_choice = int(input("Choose an option (1/2/3): ")) - 1
            vegan_preference = vegan_options[vegan_choice]
            break
        except (ValueError, IndexError):
            print("Invalid input. Please enter 1, 2, or 3.")

    print("Do you require meals at the cafe?")
    for i, option in enumerate(wifi_options, 1):
        print(f"{i}. {option.capitalize()}")
    while True:
        try:
            meals_choice = int(input("Choose an option (1/2): ")) - 1
            needs_meals = wifi_options[meals_choice]
            break
        except (ValueError, IndexError):
            print("Invalid input. Please enter 1 or 2.")

    days = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]
    print("What day of the week are you visiting?")
    for i, day in enumerate(days, 1):
        print(f"{i}. {day.capitalize()}")
    while True:
        try:
            day_choice = int(input("Choose an option (1-7): ")) - 1
            visit_day = days[day_choice]
            break
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 7.")

    while True:
        try:
            visit_start = int(
                input("Enter your arrival time (24-hour format, ex. 13 for 1 PM): ")
            )
            if 0 <= visit_start <= 24:
                break
            else:
                raise ValueError("Time must be between 0 and 24.")
        except ValueError as e:
            print(f"Invalid input: {e}")

    while True:
        try:
            visit_end = int(
                input(
                    "Enter your departure time (24-hour format, ex. 15 for 3 PM, or 26 for 2 AM the next day): "
                )
            )
            if 0 <= visit_end <= 48 and (visit_end >= visit_start or visit_end <= 24):
                break
            else:
                raise ValueError("Departure time must be valid.")
        except ValueError as e:
            print(f"Invalid input: {e}")

    return (
        transport,
        max_time,
        max_price,
        wifi,
        sockets,
        vegan_preference,
        needs_meals,
        visit_day,
        visit_start,
        visit_end,
    )


def find_cafe(
    transport,
    max_time,
    max_price,
    wifi,
    sockets,
    vegan_preference,
    needs_meals,
    visit_day,
    visit_start,
    visit_end,
):
    try:
        query = (
            f"suitable_cafe(Cafe, '{transport}', {max_time}, {max_price}, '{wifi}', '{sockets}', "
            f"'{vegan_preference}', '{needs_meals}', '{visit_day}', {visit_start}, {visit_end})"
        )
        cafes = list(prolog.query(query))

        # Retrieve addresses for each cafe found
        results = []
        for cafe_result in cafes:
            cafe_name = cafe_result["Cafe"]
            address_query = f"address('{cafe_name}', Address)"
            address_result = list(prolog.query(address_query))
            if address_result:
                # Combine the cafe_result with the address
                combined = {**cafe_result, "Address": address_result[0]["Address"]}
                results.append(combined)

        return results
    except Exception as e:
        print(f"Error querying Prolog: {e}")
        return []


def display_results(results, transport):
    """
    Displays the results of the Prolog query in a natural language format with a numbered list.

    Args:
        results (list): A list of dictionaries containing the cafes that match the query.
        transport (str): The preferred mode of transportation specified by the user.
    """
    if results:
        print("\n✨ Here are some cafes you might love! ✨\n")
        for idx, cafe in enumerate(results, 1):
            name = cafe["Cafe"].replace("_", " ")
            address = cafe["Address"].replace("_", " ")
            transport_time = cafe.get(f"{transport}_time", -1)

            if transport_time == -1:
                walk_time_query = f"walk_time('{cafe['Cafe']}', WalkTime)"
                walk_time_result = list(prolog.query(walk_time_query))
                if walk_time_result:
                    walk_time = walk_time_result[0]["WalkTime"]
                    print(
                        f"{idx}. {name} at {address} is within walking distance. It takes approximately {walk_time} minutes on foot!"
                    )
                else:
                    print(
                        f"{idx}. {name} at {address} is within walking distance, but the walking time is unknown!"
                    )
            else:
                print(
                    f"{idx}. {name} at {address} can be reached by {transport} in approximately {transport_time} minutes!"
                )

    else:
        print("\nNo suitable cafes found based on your preferences :(")


if __name__ == "__main__":
    try:
        user_input = ask_user()
        transport = user_input[0]
        results = find_cafe(*user_input)
        display_results(results, transport)
    except Exception as e:
        print(f"An error occurred: {e}")
