import tkinter as tk
from tkinter import ttk
from Transport import stability
from common import result_text

def create_risk_window(root):
    heading_label = ttk.Label(root, text="Risk Analysis", font=("Arial", 30, "bold"), foreground="black")
    heading_label.pack(pady=10, anchor="c")


    description_text = "If GO is stable and Toxicity is high then it is risky"
    description_label = tk.Label(root, text=description_text, anchor="w", wraplength=1000, bg="light blue", font=("Helvetica", 14))
    description_label.place(relx=0.05, rely=0.15, anchor=tk.W)

    if(stability == "Stable" and result_text.startswith("Toxic")):
        risk_status = "Risky"
    else:
        risk_status = "Not Risky"

    # Display the result
    risk_label = tk.Label(root, text=f"Risk Status: {risk_status}", anchor="w", wraplength=1000, bg="light blue", font=("Helvetica", 14, "bold"))
    risk_label.place(relx=0.05, rely=0.25, anchor=tk.W)