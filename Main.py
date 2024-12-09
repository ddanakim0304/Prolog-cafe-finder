from pyswip import Prolog
from generate_list import generate_cafes_prolog_file

# Replace this data with real ones plz!!!
cafe_data = [
    {
        "name": "cafe1",
        "distance": 0.5,
        "price": "low",
        "wifi": "yes",
        "sockets": "yes",
        "vegan": "yes",
        "cash_discount": "no",
        "days_opened": "[monday, tuesday, wednesday, thursday, friday]",
        "hours_opened": "[9-17]",
    }
]

# Initialize Prolog interface
prolog = Prolog()
prolog.consult("cafes.pl")

# Function to display a menu and collect user inputs
def ask_user():
    print("Welcome to the Cafe Finder Expert System!")
    print("Please answer the following questions to find the best cafe for you 🍵🫖")
    
    max_distance = float(input("Enter maximum distance from the res (in km): "))
    print("Price range options: $, $$, $$$")
    price = input("Enter your preferred price range: ").strip().lower()
    wifi = input("Do you need Wi-Fi? (yes/no): ").strip().lower()
    sockets = input("Do you need power sockets? (yes/no): ").strip().lower()
    vegan = input("Do you need vegan/vegetarian options? (yes/no): ").strip().lower()
    visit_day = input("What day of the week are you visiting? (e.g., monday): ").strip().lower()
    visit_start = int(input("Enter your arrival time (24-hour format, ex. 13 for 1 PM): "))
    visit_end = int(input("Enter your departure time (24-hour format, ex. 15 for 3 PM): "))
    
    return max_distance, price, wifi, sockets, vegan, visit_day, visit_start, visit_end

# Function to query the Prolog knowledge base
def find_cafe(max_distance, price, wifi, sockets, vegan, visit_day, visit_start, visit_end):
    query = (
        f"suitable_cafe(Cafe, {max_distance}, {price}, {wifi}, {sockets}, {vegan}, "
        f"{visit_day}, {visit_start}, {visit_end})"
    )
    results = list(prolog.query(query))
    return results

# Function to display results
def display_results(results):
    if results:
        print("\nRecommended Cafes:")
        for cafe in results:
            print(f"- {cafe['Cafe']}")
    else:
        print("\nNo suitable cafes found based on your preferences.")

# Main execution
if __name__ == "__main__":
    user_input = ask_user()
    results = find_cafe(*user_input)
    display_results(results)