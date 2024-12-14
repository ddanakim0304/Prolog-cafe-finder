def generate_cafes_prolog_file(cafe_data, output_file="cafes.pl"):
    with open(output_file, "w") as file:
        # Group facts by predicate
        predicates = {
            "address": [],
            "public_transport_time": [],
            "walk_time": [],
            "taxi_time": [],
            "price_range": [],
            "wifi": [],
            "sockets": [],
            "vegan_options": [],
            "meals": [],
            "days_opened": [],
            "open_hour": [],
            "close_hour": [],
        }

        # Populate the predicate groups
        for cafe in cafe_data:
            cafe_name = cafe["name"].replace(" ", "_")
            address = cafe["address"].replace(" ", "_")
            predicates["address"].append(f"address('{cafe_name}', '{address}').")
            predicates["public_transport_time"].append(
                f"public_transport_time('{cafe_name}', {cafe['public_transport_time']})."
            )
            predicates["walk_time"].append(
                f"walk_time('{cafe_name}', {cafe['walk_time']})."
            )
            predicates["taxi_time"].append(
                f"taxi_time('{cafe_name}', {cafe['taxi_time']})."
            )
            predicates["price_range"].append(
                f"price_range('{cafe_name}', {cafe['price_range'][0]}, {cafe['price_range'][1]})."
            )
            predicates["wifi"].append(f"wifi('{cafe_name}', '{cafe['wifi']}').")
            predicates["sockets"].append(
                f"sockets('{cafe_name}', '{cafe['sockets']}')."
            )
            vegan_opts = (
                "[" + ",".join(f"'{opt}'" for opt in cafe["vegan_vegetarian"]) + "]"
            )
            predicates["vegan_options"].append(
                f"vegan_options('{cafe_name}', {vegan_opts})."
            )
            predicates["meals"].append(f"meals('{cafe_name}', '{cafe['meals']}').")
            days_opened = (
                "[" + ",".join(f"'{day}'" for day in cafe["days_opened"]) + "]"
            )
            predicates["days_opened"].append(
                f"days_opened('{cafe_name}', {days_opened})."
            )
            open_hours = "[" + ",".join(str(h) for h in cafe["opening_hour"]) + "]"
            predicates["open_hour"].append(f"open_hour('{cafe_name}', {open_hours}).")
            close_hours = "[" + ",".join(str(h) for h in cafe["closing_hour"]) + "]"
            predicates["close_hour"].append(
                f"close_hour('{cafe_name}', {close_hours})."
            )

        # Write facts grouped by predicate
        for predicate, facts in predicates.items():
            file.write("\n".join(facts) + "\n\n")

        # Write rules with default "any" handling
        file.write("% Rules\n")
        file.write(
            "suitable_cafe(Cafe, Transport, MaxTime, MaxPrice, Wifi, Sockets, VeganPreference, NeedsMeals, VisitDay, VisitStart, VisitEnd) :-\n"
        )
        file.write("    % Check transport/time constraints\n")
        file.write("    (Transport = any -> true;\n")
        file.write("     (Transport = walk -> walk_time(Cafe, WT), WT =< MaxTime;\n")
        file.write(
            "      Transport = public_transport -> public_transport_time(Cafe, PT), (PT =< MaxTime ; PT = -1);\n"
        )
        file.write(
            "      Transport = taxi -> taxi_time(Cafe, TT), (TT =< MaxTime ; TT = -1))),\n"
        )
        file.write("\n")
        file.write("    % Check price range\n")
        file.write("    (MaxPrice = any -> true;\n")
        file.write(
            "     price_range(Cafe, MinPrice, MaxPriceRange), MaxPrice >= MinPrice, MaxPrice =< MaxPriceRange),\n"
        )
        file.write("\n")
        file.write("    % Check wifi and sockets\n")
        file.write("    (Wifi = any -> true; wifi(Cafe, Wifi)),\n")
        file.write("    (Sockets = any -> true; sockets(Cafe, Sockets)),\n")
        file.write("\n")
        file.write("    % Check vegan/vegetarian preferences\n")
        file.write("    vegan_options(Cafe, Options),\n")
        file.write("    (VeganPreference = any -> true;\n")
        file.write("     VeganPreference = vegan -> member('vegan', Options);\n")
        file.write(
            "     VeganPreference = vegetarian -> member('vegetarian', Options);\n"
        )
        file.write("     VeganPreference = none -> true),\n")
        file.write("\n")
        file.write("    % Check meals requirement\n")
        file.write("    (NeedsMeals = any -> true;\n")
        file.write("     (NeedsMeals = yes -> meals(Cafe, yes); true)),\n")
        file.write("\n")
        file.write("    % Check day and hours\n")
        file.write("    (VisitDay = any -> true;\n")
        file.write("     days_opened(Cafe, Days), member(VisitDay, Days),\n")
        file.write("     open_hour(Cafe, OpenHours), nth0(DayIndex, Days, VisitDay), nth0(DayIndex, OpenHours, Open),\n")
        file.write("     close_hour(Cafe, CloseHours), nth0(DayIndex, CloseHours, Close),\n")
        file.write("     (VisitStart = any -> true; VisitStart >= Open),\n")
        file.write("     (VisitEnd = any -> true; VisitEnd =< Close)).\n")
