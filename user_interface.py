# Import Module
from tkinter import *
from interface.start import start  # Import the start function from start.py

# # Create root window
root = Tk()

# # Root window title and dimension
# root.title("Welcome to GeekForGeeks")
# # Set geometry (widthxheight)
root.geometry("350x200")

# Call the start function to display the start interface
start = start()  # This will create the start interface
