# Import Module
from tkinter import *

from pyswip import Prolog
from generate_list import generate_cafes_prolog_file
from cafe_data import cafe_data

# Generate the cafes.pl file
generate_cafes_prolog_file(cafe_data)

# Initialize Prolog interface
prolog = Prolog()
prolog.consult("cafes.pl")


def start():
    # Create the main window
    window = Tk()

    # Create a frame for layout
    frame = Frame(window)
    frame.pack()

    # Create a frame with fixed width on the left
    img_frame = Frame(
        frame, width=200, height=200, bg="lightgray"
    )  # Fixed width and height
    img_frame.pack(side=LEFT)

    # Create a welcome label on the right
    welcome_label = Label(frame, text="Welcome to the Cafe Finder Expert System!")
    welcome_label.pack(side=RIGHT)

    # Create a continue button
    continue_button = Button(
        window, text="Continue", command=lambda: ask_transport_type(frame)
    )
    continue_button.pack()

    # Start the main loop
    window.mainloop()


def find_cafes_transport(transport):
    try:
        # Updated query to return all cafes based on transport only
        query = f"suitable_cafe(Cafe, '{transport}', 'none', 'none', 'none', 'none', 'none', 'none', 'none', 'none')"
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


def ask_transport_type(frame):
    # Remove the existing label and button
    for widget in frame.winfo_children():
        widget.destroy()

    # Create a frame with fixed width on the left
    img_frame = Frame(
        frame, width=200, height=200, bg="lightgray"
    )  # Fixed width and height
    img_frame.pack(side=LEFT)

    # Create a new label
    transport_label = Label(frame, text="Select transport type")
    transport_label.pack(side=TOP)

    # Create a dropdown menu
    transport_options = ["Car", "Bus", "Bike"]  # Example options
    transport_var = StringVar(frame)
    transport_var.set(transport_options[0])  # Set default option

    transport_dropdown = OptionMenu(frame, transport_var, *transport_options)
    transport_dropdown.pack(side=TOP)

    find_cafes_transport("Walk")

    # Create a continue button for the next step
    continue_button = Button(
        frame, text="Continue", command=lambda: ask_max_travel_time(frame)
    )
    continue_button.pack(side=TOP)


def ask_max_travel_time(frame):
    # Remove the existing label and dropdown
    for widget in frame.winfo_children():
        widget.destroy()

    # Create a frame with fixed width on the left
    img_frame = Frame(
        frame, width=200, height=200, bg="lightgray"
    )  # Fixed width and height
    img_frame.pack(side=LEFT)

    # Create a new label asking for maximum travel time
    time_label = Label(frame, text="What is your maximum travel time (in minutes)?")
    time_label.pack(side=TOP)

    # Create an entry for the user to input their maximum travel time
    time_entry = Entry(frame)
    time_entry.pack(side=TOP)

    # Create a button to submit the maximum travel time
    submit_button = Button(
        frame, text="Submit", command=lambda: submit_travel_time(time_entry.get())
    )
    submit_button.pack(side=TOP)


def submit_travel_time(max_time):
    print(f"Maximum travel time submitted: {max_time}")
    # Here you can add further logic to handle the submitted travel time
