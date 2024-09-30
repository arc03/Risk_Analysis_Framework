import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

stability = "stable"

def create_transport_tab(parent_frame):
    # Heading label
    heading_label = ttk.Label(parent_frame, text="Transport and Fate Analysis", font=("Arial", 30, "bold"), foreground="black")
    heading_label.pack(pady=10, anchor="c")

    # Create radio buttons for Terrestrial and Aqueous options in the same line
    transport_mode_var = tk.StringVar(value="Terrestrial")
    
    radio_frame = tk.Frame(parent_frame, bg="light blue")
    radio_frame.pack(pady=5, anchor="w")

    terrestrial_radio = ctk.CTkRadioButton(radio_frame, text="Terrestrial", variable=transport_mode_var, value="Terrestrial", font=("Arial", 20),text_color="black", command=lambda: update_inputs("Terrestrial"))
    terrestrial_radio.pack(side="left", padx=10)
    
    aqueous_radio = ctk.CTkRadioButton(radio_frame, text="Aqueous", variable=transport_mode_var, value="Aqueous", font=("Arial", 20), text_color="black", command=lambda: update_inputs("Aqueous"))
    aqueous_radio.pack(side="left", padx=10)
    
    # Frame for input fields
    input_frame = tk.Frame(parent_frame, bg="light blue")
    input_frame.pack(pady=10, anchor="w")

    def update_inputs(mode):
        # Clear the frame first
        for widget in input_frame.winfo_children():
            widget.destroy()

        # Initialize input fields
        nonlocal entry_pH, entry_ionic_strength, entry_humic_acid, entry_concentration, entry_size, entry_media, entry_ionic_acid, dropdown_nom, dropdown_method_of_synthesis

        ctk.CTkLabel(input_frame, text="                pH:", font=("Arial", 20), text_color="black").grid(row=0, column=0, pady=5, sticky="w")
        entry_pH = ctk.CTkEntry(input_frame, font=("Arial", 20))
        entry_pH.grid(row=0, column=1, pady=5, sticky="w")

        ctk.CTkLabel(input_frame, text="                Ionic Strength: (mg/L)", font=("Arial", 20), text_color="black").grid(row=1, column=0, pady=5, sticky="w")
        entry_ionic_strength = ctk.CTkEntry(input_frame, font=("Arial", 20))
        entry_ionic_strength.grid(row=1, column=1, pady=5, sticky="w")

        ctk.CTkLabel(input_frame, text="                Humic Acid: (mg/L)", font=("Arial", 20), text_color="black").grid(row=2, column=0, pady=5, sticky="w")
        entry_humic_acid = ctk.CTkEntry(input_frame, font=("Arial", 20))
        entry_humic_acid.grid(row=2, column=1, pady=5, sticky="w")

        ctk.CTkLabel(input_frame, text="                Concentration: (mg/L)", font=("Arial", 20), text_color="black").grid(row=3, column=0, pady=5, sticky="w")
        entry_concentration = ctk.CTkEntry(input_frame, font=("Arial", 20))
        entry_concentration.grid(row=3, column=1, pady=5, sticky="w")

        ctk.CTkLabel(input_frame, text="                Size: (nm)", font=("Arial", 20), text_color="black").grid(row=4, column=0, pady=5, sticky="w")
        entry_size = ctk.CTkEntry(input_frame, font=("Arial", 20))
        entry_size.grid(row=4, column=1, pady=5, sticky="w")

        ctk.CTkLabel(input_frame, text="                NOM:", font=("Arial", 20), text_color="black").grid(row=5, column=0, pady=5, sticky="w")
        dropdown_nom = ctk.CTkComboBox(input_frame, values=["Present", "Not Present"], font=("Arial", 20))
        dropdown_nom.grid(row=5, column=1, pady=5, sticky="w")
            
        ctk.CTkLabel(input_frame, text="                Method of Synthesis:", font=("Arial", 20), text_color="black").grid(row=6, column=0, pady=5, sticky="w")
        dropdown_method_of_synthesis = ctk.CTkComboBox(input_frame, values=[
            "Hummers Method", "Modified Hummers Method", "Brodie Method", "Staudenmaier Method", "Improved Synthesis", "CVD Method"
        ], font=("Arial", 20))
        dropdown_method_of_synthesis.grid(row=6, column=1, pady=5, sticky="w")

        if mode == "Aqueous":
            ctk.CTkLabel(input_frame, text="                Media:", font=("Arial", 20), text_color="black").grid(row=7, column=0, pady=5, sticky="w")
            entry_media = ctk.CTkEntry(input_frame, font=("Arial", 20))
            entry_media.grid(row=7, column=1, pady=5, sticky="w")

            ctk.CTkLabel(input_frame, text="                Type of Water:", font=("Arial", 20), text_color="black").grid(row=5, column=0, pady=5, sticky="w")
            dropdown_nom = ctk.CTkComboBox(input_frame, values=["Ground Water", "River Water", "Lake Water", "Tap Water"], font=("Arial", 20))
            dropdown_nom.grid(row=5, column=1, pady=5, sticky="w")

    # Initialize with Terrestrial inputs
    entry_pH = entry_ionic_strength = entry_humic_acid = entry_concentration = entry_size = entry_media = entry_ionic_acid = dropdown_nom = dropdown_method_of_synthesis = None
    update_inputs("Terrestrial")

    global stability

    # Function to check stability
    def check_stability():
        try:
            # Retrieve values from input fields
            pH_value = int(entry_pH.get())
            NOM = str(dropdown_nom.get())
            IS = int(entry_ionic_strength.get())
            HA = float(entry_humic_acid.get())
            # Check stability conditions
            if 5 <= pH_value <= 9 and IS >= 8 and NOM == "Present" and HA >= 5:
                stability = "Stable"
                result_text = f"Stability: {stability}"
                result_label.config(text=result_text, font=("Arial", 14, "bold"), fg="black")
            else:
                stability = "Not Stable"
                result_text = f"Stability: {stability}"
                result_label.config(text=result_text, font=("Arial", 14, "bold"), fg="black")
            
        except ValueError:
            result_text = "Invalid value"
            result_label.config(text=result_text, font=("Arial", 14, "bold"), fg="black")

    # Button to check stability
    check_button = ctk.CTkButton(parent_frame, text='Check Stability', corner_radius=10, command=check_stability)
    check_button.pack(pady=10, anchor="w")

    # Label to show result
    result_label = tk.Label(parent_frame, text="", bg="light blue", fg="black")
    result_label.pack(pady=10, anchor="w")

    # Image display on the right side
    # image_path = "graphene.png"
    # image = Image.open(image_path)
    # image = image.resize((700, 675))
    # photo = ImageTk.PhotoImage(image)
    # image_label = ttk.Label(parent_frame, image=photo)
    # image_label.image = photo  # Keep a reference to avoid garbage collection
    # image_label.pack(anchor="ne")
    # image_label.grid(column=2, row=1, rowspan=8, padx=20)
    # image_label.grid(column=2, row=2, rowspan=8, padx=20)

# Create main window for testing the tab function
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    root.title("Test Transport and Fate Tab")
    root.configure(bg="light blue")

    # Create a notebook for tabs
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # Create a frame for the "Transport and Fate" tab
    transport_frame = tk.Frame(notebook, bg="light blue")
    notebook.add(transport_frame, text="Transport and Fate")

    # Add the transport tab content
    create_transport_tab(transport_frame)

    root.mainloop()
