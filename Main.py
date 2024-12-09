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

# Generate the cafes.pl file
generate_cafes_prolog_file(cafe_data)

# Initialize Prolog interface
prolog = Prolog()
prolog.consult("cafes.pl")

# Function to display a menu and collect user inputs
def ask_user():
    print("Welcome to the Cafe Finder Expert System!")
    print("Please answer the following questions to find the best cafe for you 🍵")
    max_distance = float(input("Enter maximum distance from residence (in km): "))
    print("Price range options: $, $$, $$$")
    price = input("Enter your preferred price range: ").strip().lower()
    wifi = input("Do you need Wi-Fi? (yes/no): ").strip().lower()
    sockets = input("Do you need power sockets? (yes/no): ").strip().lower()
    vegan = input("Do you need vegan/vegetarian options? (yes/no): ").strip().lower()
    
    return max_distance, price, wifi, sockets, vegan

# Function to query the Prolog knowledge base
def find_cafe(max_distance, price, wifi, sockets, vegan):
    query = f"suitable_cafe(Cafe, {max_distance}, {price}, {wifi}, {sockets}, {vegan})"
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
    max_distance, price, wifi, sockets, vegan = ask_user()
    results = find_cafe(max_distance, price, wifi, sockets, vegan)
    display_results(results)
