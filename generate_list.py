def generate_cafes_prolog_file(cafe_data, output_file="cafes.pl"):
    with open(output_file, "w") as file:
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
            file.write(f"open_hour({cafe_name}, {cafe['open_hour']}).\n")
            file.write(f"close_hour({cafe_name}, {cafe['close_hour']}).\n\n")

        # Add rules
        file.write("% Rules\n")
        file.write("suitable_cafe(Cafe, MaxDistance, Price, Wifi, Sockets, Vegan, VisitDay, VisitStart, VisitEnd) :-\n")
        file.write("    distance(Cafe, D), D =< MaxDistance,\n")
        file.write("    price(Cafe, Price),\n")
        file.write("    wifi(Cafe, Wifi),\n")
        file.write("    sockets(Cafe, Sockets),\n")
        file.write("    vegan(Cafe, Vegan),\n")
        file.write("    days_opened(Cafe, Days), member(VisitDay, Days),\n")
        file.write("    open_hour(Cafe, Open), close_hour(Cafe, Close),\n")
        file.write("    VisitStart >= Open, VisitEnd =< Close.\n")