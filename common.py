import pandas as pd
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter as ctk

# Dummy stability variable for demonstration
stability = "Stable"
result_text = "Toxic"
def process_input():
    species = species_var.get()
    concentration = concentration_entry.get()
    crawling_assay = crawling_entry.get()
    climbing_assay = climbing_entry.get()
    longevity_assay = longevity_entry.get()
    phenotypic_abnormalities = phenotypic_dropdown.get()


    if concentration.isdigit():
        result_text = get_class(species, concentration, crawling_assay, climbing_assay, longevity_assay, phenotypic_abnormalities, stability)
        # Change the color based on the result
        output_label.config(text=result_text, fg="green" if "Toxic" in result_text else "blue")
    else:
        output_label.config(text="Please enter valid inputs", fg="red")

def get_class(species, concentration, crawling_assay, climbing_assay, longevity_assay, phenotypic_abnormalities, trans):
    df = pd.read_excel('Frame.xlsx')
    filtered_df = df[(df['Species'] == species) & (df['Concentration'] <= int(concentration)) & (trans == "Stable")]
    if not filtered_df.empty:
        return "Toxic: " + filtered_df['Classes'].values[0]
    else:
        return 'Non Toxic'

def create_main2_window(root):
    global species_var, concentration_entry, crawling_entry, climbing_entry, longevity_entry, phenotypic_dropdown, output_label

    # Load species data from Excel
    df = pd.read_excel('Frame.xlsx')
    species_list = df['Species'].unique().tolist() if 'Species' in df.columns else []

    # Setup themed style
    style = ttk.Style(root)
    style.configure("TLabel", font=("Arial", 12))
    style.configure("TButton", font=("Arial", 12))

    # Create a canvas and a scrollbar
    canvas = tk.Canvas(root, bg="light blue")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

    # Create a frame inside the canvas
    main_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=main_frame, anchor="nw")

    # Add heading at the top of the main_frame
    heading_label = tk.Label(main_frame, text="Risk Analysis Framework for Nanomaterials (Graphene Oxide (GO))", font=("Arial", 16, "bold"))
    heading_label.grid(column=0, row=0, columnspan=3, pady=20)

    # Add input fields
    species_label = tk.Label(main_frame, text='Select Species:', font=("Arial", 12))
    species_label.grid(column=0, row=1, sticky=tk.W)
    species_var = tk.StringVar(root)
    species_dropdown = ttk.Combobox(main_frame, textvariable=species_var, values=species_list, width=50)
    species_dropdown.grid(column=1, row=1, pady=10)

    concentration_label = tk.Label(main_frame, text='Enter Concentration (In mg/L)', font=("Arial", 12))
    concentration_label.grid(column=0, row=2, sticky=tk.W)
    concentration_entry = tk.Entry(main_frame)
    concentration_entry.grid(column=1, row=2, pady=10)

    crawling_label = tk.Label(main_frame, text='Enter Crawling Assay:', font=("Arial", 12))
    crawling_label.grid(column=0, row=3, sticky=tk.W)
    crawling_entry = tk.Entry(main_frame)
    crawling_entry.grid(column=1, row=3, pady=10)

    climbing_label = tk.Label(main_frame, text='Enter Climbing Assay:', font=("Arial", 12))
    climbing_label.grid(column=0, row=4, sticky=tk.W)
    climbing_entry = tk.Entry(main_frame)
    climbing_entry.grid(column=1, row=4, pady=10)

    longevity_label = tk.Label(main_frame, text='Enter Longevity Assay:', font=("Arial", 12))
    longevity_label.grid(column=0, row=5, sticky=tk.W)
    longevity_entry = tk.Entry(main_frame)
    longevity_entry.grid(column=1, row=5, pady=10)

    phenotypic_label = tk.Label(main_frame, text='Select Phenotypic Abnormalities:', font=("Arial", 12))
    phenotypic_label.grid(column=0, row=6, sticky=tk.W)
    phenotypic_dropdown = ttk.Combobox(main_frame, values=["F0", "F1", "F2"], width=50)
    phenotypic_dropdown.grid(column=1, row=6, pady=10)

    # Process button
    process_button = ctk.CTkButton(main_frame, text='Process', corner_radius=10, command=process_input)
    process_button.grid(column=1, row=7, pady=20, sticky=tk.E)

    # Output label
    output_label = tk.Label(main_frame, text='', font=("Arial", 12))
    output_label.grid(column=0, row=8, columnspan=2)

    # Image display on the right side
    image_path = "Toxicity.png"
    image = Image.open(image_path)
    image = image.resize((600, 600))
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(main_frame, image=photo)
    image_label.image = photo  # Keep a reference to avoid garbage collection
    image_label.grid(column=2, row=1, rowspan=8, padx=20)

    # Ensure the last widget is always visible
    main_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

# Create main window for testing the function
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1200x675")
    root.title("Risk Analysis Framework")

    create_main2_window(root)
    root.mainloop()
