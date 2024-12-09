def generate_cafes_prolog_file(cafe_data, output_file="cafes.pl"):
    with open(output_file, "w") as file:
        file.write("% Automatically generated Prolog knowledge base for cafes\n\n")

        # Add facts
        for cafe in cafe_data:
            cafe_name = cafe["name"]
            file.write(f"distance({cafe_name}, {cafe['distance']}).\n")
            file.write(f"price({cafe_name}, {cafe['price']}).\n")
            file.write(f"wifi({cafe_name}, {cafe['wifi']}).\n")
            file.write(f"sockets({cafe_name}, {cafe['sockets']}).\n")
            file.write(f"vegan({cafe_name}, {cafe['vegan']}).\n")
            file.write(f"cash_discount({cafe_name}, {cafe['cash_discount']}).\n")
            file.write(f"days_opened({cafe_name}, {cafe['days_opened']}).\n")
            file.write(f"hours_opened({cafe_name}, {cafe['hours_opened']}).\n\n")

        # Add rules
        file.write("% Rules\n")
        file.write("suitable_cafe(Cafe, MaxDistance, Price, Wifi, Sockets, Vegan) :-\n")
        file.write("    distance(Cafe, D), D =< MaxDistance,\n")
        file.write("    price(Cafe, Price),\n")
        file.write("    wifi(Cafe, Wifi),\n")
        file.write("    sockets(Cafe, Sockets),\n")
        file.write("    vegan(Cafe, Vegan).\n")

# Example cafe (please remove this and add actual data!)
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

# Generate the Prolog file
generate_cafes_prolog_file(cafe_data)
