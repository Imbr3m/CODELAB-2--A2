import tkinter as tk

# The window!
root = tk.Tk()

root.title("Pokedex")
root.geometry("800x500")
root.configure(background = "purple")


#Dummy information to test the search button
pokedex = {
    "bulbasaur": ["bulbasaur", "grass", "poison", 15, 15, "Grass Starter", 3.8],
    "squirtle": ["squirtle", "water", "none", 10, 10, "Water Starter", 5.9],
    "charmander": ["charmander", "fire", "none", 25, 25, "Fire Starter", 7.3]
}

def select_pokemon():
    # gets the text typed into the Entry widget
    selected = submit_entry.get()
    
    # updates the text variable of the relevant labels with the appropriate information
    
    # The name
    name_text["text"] = pokedex[selected][0]
    
    # The types
    type1label["text"] = pokedex[selected][1]
    type2label["text"] = pokedex[selected][2]
    
    # the height, weight, species, and catch rate
    height_entry["text"] = pokedex[selected][3]
    weight_entry["text"] = pokedex[selected][4]
    species_entry["text"] = pokedex[selected][5]
    catch_entry["text"] = str(pokedex[selected][6]) + "chance to catch with a Pokeball"


# Configure 4 rows and 3 columns.
root.rowconfigure([i for i in range(4)], minsize = 50, weight = 1)
root.columnconfigure([i for i in range(3)], minsize = 50, weight = 1)

### Name Frame
# Name Frame
name_label = tk.Frame(root, relief=tk.RAISED, borderwidth=4)
name_text = tk.Label(name_label, text="Pokemon Name Here", font=("Futura", 16))
name_text.pack()
name_label.grid(row=0, column=2)


### Picture Frame
picture_frame = tk.Frame(root, relief = tk.SUNKEN, borderwidth = 2)
label = tk.Label(picture_frame, text = "Pokemon Picture Here", font = ("Futura", 16))
label.pack()
picture_frame.grid(row = 1, column = 2, rowspan = 2, sticky = "ns")

### Type Frame
type_frame = tk.Frame(root, relief = tk.RAISED, borderwidth = 2)
type1label = tk.Label(type_frame, text = "Type 1 Here", font = ("Futura", 12))
type1label.grid(row = 0, column = 0)
type2label = tk.Label(type_frame, text = "Type 2 Here", font = ("Futura", 12))
type2label.grid(row = 0, column = 1)
type_frame.grid(row = 3, column = 2)

### Search Frame
search_frame = tk.Frame(root, relief = tk.RAISED, borderwidth = 2)


search_frame.columnconfigure([0,1,2,3], weight = 1)

# I converted this to a button
left_button = tk.Button(search_frame, text = "Left Arrow", font = ("Futura", 16))
left_button.grid(row = 0, column = 0)

# made an entry box for users to type latr
# Give it a relevant name so that we can use it.
submit_entry = tk.Entry(search_frame, font = ("Futura", 16))
submit_entry.grid(row = 0, column = 1)

submit_button = tk.Button(search_frame, text = "Search!", font = ("Futura", 16), command = select_pokemon)
submit_button.grid(row = 0, column = 2)

# Converted this to a th right button
right_button = tk.Button(search_frame, text = "Right Arrow", font = ("Futura", 16))
right_button.grid(row = 0, column = 3)

search_frame.grid(row = 0, column = 0, columnspan = 2, sticky = "ew")

### Info Frame
info_frame = tk.Frame(root, relief = tk.SUNKEN, borderwidth = 4)

# Calling rowconfigure and columnfigure within the info_frame
# causes the contents of the frame (label) to be centered within it.
info_frame.rowconfigure([0,1,2], weight = 1)
info_frame.columnconfigure([0,1], weight = 1)

## Various Information

# The Pokedex entry is long, so we'll let it take up two columns
pokedex_entry = tk.Label(info_frame, text = "Pokedex Entry", font = ("Futura", 16))
pokedex_entry.grid(row = 0, column = 0, columnspan = 2)

height_entry = tk.Label(info_frame, text = "Height", font = ("Futura", 16))
height_entry.grid(row = 1, column = 0)

weight_entry = tk.Label(info_frame, text = "Weight", font = ("Futura", 16))
weight_entry.grid(row = 1, column = 1)

species_entry = tk.Label(info_frame, text = "Species", font = ("Futura", 16))
species_entry.grid(row = 2, column = 0)

catch_entry = tk.Label(info_frame, text = "Catch Rate", font = ("Futura", 16))
catch_entry.grid(row = 2, column = 1)

info_frame.grid(row = 1, rowspan = 3, column = 0, columnspan = 2, sticky = "nsew")

# Run the App
root.mainloop()