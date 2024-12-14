# Import Module
from tkinter import *

import os


def transport():
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
    continue_button = Button(window, text="Continue", command=window.quit)
    continue_button.pack()

    # Start the main loop
    # window.mainloop()
