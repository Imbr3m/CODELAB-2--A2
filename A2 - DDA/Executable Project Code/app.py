from PIL import Image, ImageTk  # Import for handling images
from io import BytesIO  # To handle image byte data
import os #debuggin

import requests
import tkinter as tk

# The window!
root = tk.Tk()

root.title("Pokedex")
root.geometry("800x500")
root.configure(background = "purple")


root.configure(background="purple")

# base url for the api
base_url = "https://pokeapi.co/api/v2/"

# global pokemon id
current_pokemon_id = 1

### FUNCTIONS

#For debugg reasons idk why the pokemon logo isnt showing up
image_path = r"A2 - DDA\Executable Project Code\assets\imgs\pokemon-logo-black-transparent.png"
if os.path.exists(image_path):
    print("File found!")
    pokemon_title_image = Image.open(image_path)
else:
    print(f"File not found: {image_path}")




# Fetches info from the API
def get_pokemon_info(identifier):
    url = f"{base_url}/pokemon/{identifier}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to receive data: {response.status_code}")
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
        height_entry["text"] = f"Height: {data['height']}m"
        weight_entry["text"] = f"Weight: {data['weight']}kg"
        id_entry["text"] = f"ID: {data['id']}"

        # updates stats
        stats = data.get('stats', [])
        stats_text = "\n".join([f"{stat['stat']['name'].capitalize()}: {stat['base_stat']}" for stat in stats])
        stats_entry["text"] = f"Stats:\n{stats_text}"
        
         # updates the image
        image_url = data['sprites']['front_default']
        if image_url:
            # Fetch the image
            response = requests.get(image_url)
            img_data = response.content

            # Open the image using PIL
            img = Image.open(BytesIO(img_data))
            img = img.resize((200, 200))  # Resize the image to fit in the UI
            photo = ImageTk.PhotoImage(img)

            # Update the label with the new image
            label.config(image=photo)
            label.image = photo  # Keep a reference to the image to prevent it from being garbage collected
    else:
        # Reset UI if no data is found
        name_text["text"] = "Not Found"
        type1label["text"] = "Type 1: N/A"
        type2label["text"] = "Type 2: N/A"
        height_entry["text"] = "Height: N/A"
        weight_entry["text"] = "Weight: N/A"
        id_entry["text"] = "ID: N/A"
        stats_entry["text"] = "Stats: N/A"
        label.config(image="")  # will remoove image if nothin

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
            data = get_pokemon_info(user_input)
            if data:
                current_pokemon_id = data['id']

    data = get_pokemon_info(current_pokemon_id)
    update_ui(data)

### TKINTER

# Configure 4 rows and 3 columns.
root.rowconfigure([i for i in range(4)], minsize=50, weight=1)
root.columnconfigure([i for i in range(3)], minsize=50, weight=1)

# Name Frame
name_label = tk.Frame(root, relief=tk.RAISED, borderwidth=4)
name_text = tk.Label(name_label, text="Pokemon Name Here", font=("Futura", 16))
name_text.pack()
name_label.grid(row=0, column=2)

# Picture Frame
picture_frame = tk.Frame(root, relief=tk.SUNKEN, borderwidth=2)
label = tk.Label(picture_frame, text="Pokemon Picture Here", font=("Futura", 16))
label.pack()
picture_frame.grid(row=1, column=2, rowspan=2, sticky="ns")

# Type Frame
type_frame = tk.Frame(root, relief=tk.RAISED, borderwidth=2)
type1label = tk.Label(type_frame, text="Type 1 Here", font=("Futura", 12))
type1label.grid(row=0, column=0)
type2label = tk.Label(type_frame, text="Type 2 Here", font=("Futura", 12))
type2label.grid(row=0, column=1)
type_frame.grid(row=3, column=2)

# Search Frame
search_frame = tk.Frame(root, relief=tk.RAISED, borderwidth=2)
search_frame.columnconfigure([0, 1, 2, 3], weight=1)

left_button = tk.Button(search_frame, text="Left Arrow", font=("Futura", 16), command=lambda: select_pokemon(move="backward"))
left_button.grid(row=0, column=0)

submit_entry = tk.Entry(search_frame, font=("Futura", 16))
submit_entry.grid(row=0, column=1)

submit_button = tk.Button(search_frame, text="Search!", font=("Futura", 16), command=lambda: select_pokemon())
submit_button.grid(row=0, column=2)

right_button = tk.Button(search_frame, text="Right Arrow", font=("Futura", 16), command=lambda: select_pokemon(move="forward"))
right_button.grid(row=0, column=3)

search_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

# Info Frame
info_frame = tk.Frame(root, relief=tk.SUNKEN, borderwidth=4)
info_frame.rowconfigure([0, 1, 2], weight=1)
info_frame.columnconfigure([0, 1], weight=1)

# Load the image
image_path = r"C:\Users\raine\CODELAB-2--A2\A2 - DDA\Executable Project Code\assets\imgs\pokemon-logo-black-transparent.png"

pokemon_title_image = Image.open(image_path)
pokemon_title_image = pokemon_title_image.resize((200, 100))  

pokemon_title_photo = ImageTk.PhotoImage(pokemon_title_image)

pokedex_logo = tk.Label(info_frame, image=pokemon_title_photo)
pokedex_logo.image = pokemon_title_photo  
pokedex_logo.grid(row=0, column=0, columnspan=2)

height_entry = tk.Label(info_frame, text="Height", font=("Futura", 16))
height_entry.grid(row=1, column=0)

weight_entry = tk.Label(info_frame, text="Weight", font=("Futura", 16))
weight_entry.grid(row=1, column=1)

id_entry = tk.Label(info_frame, text="ID", font=("Futura", 16))
id_entry.grid(row=2, column=0)

stats_entry = tk.Label(info_frame, text="Stats", font=("Futura", 16), justify="left")
stats_entry.grid(row=2, column=1)

info_frame.grid(row=1, rowspan=3, column=0, columnspan=2, sticky="nsew")

# Run the App
root.mainloop()
