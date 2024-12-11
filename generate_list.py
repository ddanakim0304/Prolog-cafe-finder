def generate_cafes_prolog_file(cafe_data, output_file="cafes.pl"):
    with open(output_file, "w") as file:
        # Add facts
        for cafe in cafe_data:
            cafe_name = cafe["name"].replace(" ", "_")  # Replace spaces with underscores for Prolog compatibility
            address = cafe["address"].replace(" ", "_")
            file.write(f"address({cafe_name}, '{address}').\n")
            file.write(f"public_transport_time({cafe_name}, {cafe['public_transport_time']}).\n")
            file.write(f"walk_time({cafe_name}, {cafe['walk_time']}).\n")
            file.write(f"taxi_time({cafe_name}, {cafe['taxi_time']}).\n")
            file.write(f"price_range({cafe_name}, {cafe['price_range'][0]}, {cafe['price_range'][1]}).\n")
            file.write(f"wifi({cafe_name}, {cafe['wifi']}).\n")
            file.write(f"sockets({cafe_name}, {cafe['sockets']}).\n")
            file.write(f"vegan_options({cafe_name}, {cafe['vegan_vegetarian']}).\n")
            file.write(f"meals({cafe_name}, {cafe['meals']}).\n")
            days_opened = ", ".join(cafe["days_opened"])
            file.write(f"days_opened({cafe_name}, [{days_opened}]).\n")
            open_hours = ", ".join(map(str, cafe["opening_hour"]))
            file.write(f"open_hour({cafe_name}, [{open_hours}]).\n")
            close_hours = ", ".join(map(str, cafe["closing_hour"]))
            file.write(f"close_hour({cafe_name}, [{close_hours}]).\n\n")

        # Add rules
        file.write("% Rules\n")
        file.write("suitable_cafe(Cafe, Transport, MaxTime, MaxPrice, Wifi, Sockets, VeganPreference, NeedsMeals, VisitDay, VisitStart, VisitEnd) :-\n")
        file.write("    (Transport = walk -> walk_time(Cafe, WT), WT =< MaxTime ;\n")
        file.write("     (Transport = public_transport -> public_transport_time(Cafe, PT), (PT =< MaxTime ; PT = -1));\n")
        file.write("     (Transport = taxi -> taxi_time(Cafe, TT), (TT =< MaxTime ; TT = -1))),\n")
        file.write("    price_range(Cafe, MinPrice, MaxPriceRange), MaxPrice >= MinPrice, MaxPrice =< MaxPriceRange,\n")
        file.write("    wifi(Cafe, Wifi),\n")
        file.write("    sockets(Cafe, Sockets),\n")
        file.write("    (VeganPreference = vegan -> vegan_options(Cafe, [vegan]) ; vegan_options(Cafe, [vegan, vegetarian])),\n")
        file.write("    (NeedsMeals = yes -> meals(Cafe, yes) ; true),\n")
        file.write("    days_opened(Cafe, Days), member(VisitDay, Days),\n")
        file.write("    open_hour(Cafe, OpenHours), nth0(DayIndex, Days, VisitDay), nth0(DayIndex, OpenHours, Open),\n")
        file.write("    close_hour(Cafe, CloseHours), nth0(DayIndex, CloseHours, Close),\n")
        file.write("    VisitStart >= Open, VisitEnd =< Close.\n")
