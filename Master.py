import tkinter as tk
from tkinter import PhotoImage, Label,ttk
from tkinter.ttk import Combobox, Scrollbar, Notebook, Frame
from PIL import Image, ImageTk
import customtkinter as Ctk
import Main2  
import Transport
import Risk

# Create a Tk() object
master = tk.Tk()
master.title('Risk Analysis Framework')
master.geometry("1400x700")
master.iconbitmap("Risk.ico")

def load_icon(image_path):
    image = Image.open(image_path)
    image = image.resize((20, 20), Image.LANCZOS)  # Adjust the size as needed
    return ImageTk.PhotoImage(image)

# Create icons for tabs
about_icon = load_icon("about_icon.png")  # Replace with your icon file path
transport_icon = load_icon("transport_icon.png")  # Replace with your icon file path
toxicity_icon = load_icon("toxicity_icon.png")  # Replace with your icon file path
risk_icon = load_icon("risk_icon.png")  # Replace with your icon file path

notebook = Notebook(master)
notebook.pack(fill='both', expand=True)

# Apply styles for tab text
style = ttk.Style()
style.configure('TNotebook.Tab', font=('Arial', 12, 'bold'))  # Adjust font size and style as needed

# Create tabs with icons
about_frame = tk.Frame(notebook, bg="light blue")
notebook.add(about_frame, text="About", image=about_icon, compound="left")

transport_frame = tk.Frame(notebook, bg="light blue")
notebook.add(transport_frame, text="Transport and Fate", image=transport_icon, compound="left")

toxicity_frame = tk.Frame(notebook, bg="light blue")
notebook.add(toxicity_frame, text="Toxicity Check", image=toxicity_icon, compound="left")

risk_frame = tk.Frame(notebook, bg="light blue")
notebook.add(risk_frame, text="Risk", image=risk_icon, compound="left")

# Create a notebook for tabs


# Create the "About" tab
# about_frame = tk.Frame(notebook , bg="light blue")
# notebook.add(about_frame, text="About")

# # Create the "Transport and Fate" tab
# transport_frame = tk.Frame(notebook , bg="light blue")
# notebook.add(transport_frame, text="Transport and Fate")

# # Create the "Toxicity Check" tab
# toxicity_frame = tk.Frame(notebook , bg="light blue")
# notebook.add(toxicity_frame, text="Toxicity Check")

# Risk_frame = tk.Frame(notebook , bg="light blue")
# notebook.add(Risk_frame, text="Risk")

# About Tab Content
# Create a main frame for all the content
main_frame = tk.Frame(about_frame , bg="light blue")
main_frame.place(relwidth=1, relheight=1)

# Create a top label
label = tk.Label(main_frame, text="Risk Analysis Framework of Graphene Oxide(GO)", font=("Helvetica", 20) , bg="light blue")
label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

# Description text
text_label = tk.Label(main_frame, text="Graphene Oxide", font=("Helvetica", 14), anchor="w" , bg="light blue")
text_label.place(relx=0.05, rely=0.1, anchor=tk.W)

description_text = (
    "Graphene oxide (GO) is a derivative of graphene, which is a single layer of carbon atoms arranged in a hexagonal lattice. GO is distinct from pristine graphene due to the presence of oxygen-containing functional groups such as hydroxyl, epoxy, and carboxyl groups. These functional groups impart GO with unique properties that differentiate it from graphene."
)

description_label = tk.Label(main_frame, text=description_text, anchor="w", justify=tk.LEFT, wraplength=1000 , bg="light blue", font=("Helvetica", 14))
description_label.place(relx=0.05, rely=0.15, anchor=tk.W)

# Dropdown for selecting species
species_label = tk.Label(main_frame, text='Select Layers:', font=("Arial", 12) , bg="light blue")
species_label.place(relx=0.05, rely=0.3, anchor=tk.W)
species_var = tk.StringVar(main_frame)
species_dropdown = Combobox(main_frame, textvariable=species_var, values=["Multi Layered (CFEES)", "Few Layered", "Single Layered"], width=40)
species_dropdown.place(relx=0.3, rely=0.3, anchor=tk.W)

# Scrollable table
table_canvas = tk.Canvas(main_frame , bg="light blue")
table_canvas.place(relx=0.05, rely=0.4, relwidth=0.85, relheight=0.4)
scrollbar = Scrollbar(main_frame, orient="vertical", command=table_canvas.yview)
scrollbar.place(relx=0.9, rely=0.4, relheight=0.4, anchor=tk.NW)
scrollable_frame = tk.Frame(table_canvas , bg="light blue")

scrollable_frame.bind(
    "<Configure>",
    lambda e: table_canvas.configure(
        scrollregion=table_canvas.bbox("all")
    )
)

table_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
table_canvas.configure(yscrollcommand=scrollbar.set)

# Table headers
table_headers = ["Characteristic", "Description"]
for col_num, header in enumerate(table_headers):
    header_label = tk.Label(scrollable_frame, text=header, font=("Helvetica", 14, "bold") , bg="light blue")
    header_label.grid(row=0, column=col_num, padx=5, pady=5, sticky='w')

# Table content
table_data = [
    ("Chemical Structure", "Contains oxygen functional groups: hydroxyl, epoxy, carbonyl, and carboxyl."),
    ("Morphology", "Wrinkled"),
    ("Color", "Black powder"),
    ("Hybridization", "sp²"),
    ("UV - Vis Peak", "272 nm"),
    ("Functional gap peak", "3272 cm⁻¹ (O-H Group), 1635 cm⁻¹ (C=O Stretching), 1193 and 966 cm⁻¹ (C-O-C Bending)"),
    ("Raman Bands", "D - Band at 1353.7 cm⁻¹, G - Band at 1584.8 cm⁻¹, 2D - Band at 2835.3 cm⁻¹"),
    ("Oxygen/Carbon (O/C) ratio", "0.51"),
    ("Thermal Properties", "Reduction of mass 95.22% in presence of air"),
    ("Hydrodynamic Size", "595.79 nm"),
    ("Zeta Potential", "-22.63 mV"),
    ("Electrical Properties", "Poor conductor/insulator, conductivity can be partially restored by reduction."),
    ("Mechanical Properties", "Good mechanical strength, can reinforce composites."),
    ("Solubility/Dispersibility", "Hydrophilic, disperses well in water and polar solvents, stability affected by pH and ionic strength."),
    ("Chemical Reactivity", "Reactive sites for further modifications, enabling functionalization with various groups."),
    ("Synthesis", "Typically synthesized via oxidation of graphite, commonly using the Hummers' method."),
    ("Applications", "Drug delivery, biosensing, water treatment, environmental sensors, supercapacitors, batteries, polymer and ceramic composites, flexible electronics, transparent conductors.")
]

# Add table data
for row_num, row_data in enumerate(table_data, start=1):
    for col_num, cell_data in enumerate(row_data):
        cell_label = tk.Label(scrollable_frame, text=cell_data, font=("Helvetica", 12) , bg="light blue", wraplength=900, justify=tk.LEFT)
        cell_label.grid(row=row_num, column=col_num, padx=5, pady=5, sticky='w')

# Add content to "Transport and Fate" tab
Transport.create_transport_tab(transport_frame)

# Add content to "Toxicity Check" tab
Main2.create_main2_window(toxicity_frame)

Risk.create_risk_window(risk_frame)

# Run the main loop
master.mainloop()
