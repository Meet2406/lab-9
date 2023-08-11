""" 
Description: 
  Graphical user interface that displays select information about a 
  user-specified Pokemon fetched from the PokeAPI 

Usage:
  python poke_info_viewer.py
"""
from tkinter import *
from tkinter import ttk
from poke_api import get_pokemon_info
from tkinter import messagebox

# Create the main window
root = Tk()
root.title("Pokemon Information")

# TODO: Create the frames
frame_input = ttk.Frame(root)
frame_input.grid(row=1, column=0, columnspan=2, pady=(20,1))

frame_info = ttk.LabelFrame(root, text='Info')
frame_input.grid(row=1, column=0, padx=(10,20), pady=(10,20), sticky=N)

label_name = ttk.Entry(frame_input, text="Pokemon Name")
label_name.grid(row=0, column=0, padx=(10,5), pady=(10,))

enter_name = ttk.Entry(frame_input)
enter_name.insert(0,'Charmander')
enter_name.grid(row=0,column=1)



# TODO: Define button click event handler function
def handle_button_get_info():
  poke_name = enter_name.get().strip()
  poke_st_data = {
    'name': 'Charmander',
    'types': ['Fire']
  }

# Populate the user input frame with widgets

info_btn= ttk.Button(frame_input, text="Get Info", command=handle_button_get_info)
info_btn.grid(row=0, column=2, padx=15, pady=15)


root.mainloop()