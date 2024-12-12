import tkinter as tk

# The window!
root = tk.Tk()

root.title("Pokedex")
root.geometry("800x500")
root.configure(background = "purple")

# Configure 4 rows and 3 columns.
root.rowconfigure([i for i in range(4)], minsize = 50, weight = 1)
root.columnconfigure([i for i in range(3)], minsize = 50, weight = 1)

### Name Frame
name_frame = tk.Frame(root, relief = tk.RAISED, borderwidth = 4)
label = tk.Label(name_frame, text = "Pokemon Name Here", font = ("Futura", 16))
# One of the few cases where you can mix pack() with grid().
label.pack()
name_frame.grid(row = 0, column = 0)

### Picture Frame
picture_frame = tk.Frame(root, relief = tk.SUNKEN, borderwidth = 2)
label = tk.Label(picture_frame, text = "Pokemon Picture Here", font = ("Futura", 16))
label.pack()
picture_frame.grid(row = 1, column = 0, rowspan = 2, sticky = "ns")

### Type Frame
type_frame = tk.Frame(root, relief = tk.RAISED, borderwidth = 2)
type1label = tk.Label(type_frame, text = "Type 1 Here", font = ("Futura", 12))
type1label.grid(row = 0, column = 0)
type2label = tk.Label(type_frame, text = "Type 2 Here", font = ("Futura", 12))
type2label.grid(row = 0, column = 1)
type_frame.grid(row = 3, column = 0)



# Run the App
root.mainloop()