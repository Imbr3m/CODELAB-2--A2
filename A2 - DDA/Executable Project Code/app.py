

import requests

import tkinter as tk

# The window!
root = tk.Tk()

root.title("Pokedex")
root.geometry("800x500")
root.configure(background = "purple")

##
base_url = "https://pokeapi.co/api/v2/"

# global variable to track the current Pokémon ID
current_pokemon_id = 1

###Functions

#fetches info from the API
def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else: 
        print(f"Failed to recieve data {response.status_code}")
        return None


def update_ui(data):
    if data:
        # Update the UI with Pokémon data
        name_text["text"] = data.get("name", "Unknown").capitalize()
        type1label["text"] = f"Type 1: {data['types'][0]['type']['name']}"
        type2label["text"] = (
            f"Type 2: {data['types'][1]['type']['name']}"
            if len(data['types']) > 1 else "Type 2: None"
        )
        height_entry["text"] = f"Height: {data['height']}"
        weight_entry["text"] = f"Weight: {data['weight']}"
        id_entry["text"] = f"ID: {data['id']}"
        catch_entry["text"] = "Catch Rate: N/A"  # Placeholder (not in basic API response)
    else:
        # Reset UI if no data is found
        name_text["text"] = "Not Found"
        type1label["text"] = "Type 1: N/A"
        type2label["text"] = "Type 2: N/A"
        height_entry["text"] = "Height: N/A"
        weight_entry["text"] = "Weight: N/A"
        id_entry["text"] = "ID: N/A"
        catch_entry["text"] = "Catch Rate: N/A"

def select_pokemon(move=None):
    global current_pokemon_id

    if move == "forward":
        current_pokemon_id += 1
    elif move == "backward" and current_pokemon_id > 1:
        current_pokemon_id -= 1
    else:
        user_input = submit_entry.get().strip().lower()
        if user_input.isdigit():
            current_pokemon_id = int(user_input)
        else:
            # Fetch Pokémon data by name
            data = get_pokemon_info(user_input)
            if data:
                current_pokemon_id = data['id']
            else:
                # Handle invalid input gracefully
                update_ui(None)
                return

    # Fetch Pokémon data by ID and update UI
    data = get_pokemon_info(current_pokemon_id)
    update_ui(data)


###TKINTER



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
left_button = tk.Button(search_frame, text = "Left Arrow", font = ("Futura", 16), command = lambda: select_pokemon(move = 'backward'))
left_button.grid(row = 0, column = 0)

# made an entry box for users to type latr
# Give it a relevant name so that we can use it.
submit_entry = tk.Entry(search_frame, font = ("Futura", 16))
submit_entry.grid(row = 0, column = 1)

submit_button = tk.Button(search_frame, text = "Search!", font = ("Futura", 16), command = select_pokemon)
submit_button.grid(row = 0, column = 2)

# Converted this to a th right button
right_button = tk.Button(search_frame, text = "Right Arrow", font = ("Futura", 16), command = lambda: select_pokemon(move = 'forward'))
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

id_entry = tk.Label(info_frame, text = "ID", font = ("Futura", 16))
id_entry.grid(row = 2, column = 0)

catch_entry = tk.Label(info_frame, text = "Catch Rate", font = ("Futura", 16))
catch_entry.grid(row = 2, column = 1)

info_frame.grid(row = 1, rowspan = 3, column = 0, columnspan = 2, sticky = "nsew")

# Run the App
root.mainloop()