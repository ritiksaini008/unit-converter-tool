import tkinter as tk
from tkinter import ttk, messagebox


# ==========================
# Conversion Functions
# ==========================

def convert():
    try:
        value = float(entry_value.get())

        category = category_var.get()
        from_unit = from_var.get()
        to_unit = to_var.get()

        result = 0

        # Length
        if category == "Length":
            length = {
                "Meter": 1,
                "Kilometer": 1000,
                "Centimeter": 0.01,
                "Millimeter": 0.001
            }

            result = value * length[from_unit] / length[to_unit]

        # Weight
        elif category == "Weight":
            weight = {
                "Kilogram": 1,
                "Gram": 0.001,
                "Pound": 0.453592,
                "Ton": 1000
            }

            result = value * weight[from_unit] / weight[to_unit]

        # Temperature
        elif category == "Temperature":

            if from_unit == "Celsius" and to_unit == "Fahrenheit":
                result = (value * 9/5) + 32

            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                result = (value - 32) * 5/9

            elif from_unit == "Celsius" and to_unit == "Kelvin":
                result = value + 273.15

            elif from_unit == "Kelvin" and to_unit == "Celsius":
                result = value - 273.15

            elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                result = ((value - 32) * 5/9) + 273.15

            elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                result = ((value - 273.15) * 9/5) + 32

            else:
                result = value

        result_label.config(
            text=f"Result: {round(result, 4)}"
        )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter a valid number."
        )


# ==========================
# Update Units
# ==========================

def update_units(event=None):

    category = category_var.get()

    if category == "Length":

        units = [
            "Meter",
            "Kilometer",
            "Centimeter",
            "Millimeter"
        ]

    elif category == "Weight":

        units = [
            "Kilogram",
            "Gram",
            "Pound",
            "Ton"
        ]

    else:

        units = [
            "Celsius",
            "Fahrenheit",
            "Kelvin"
        ]

    from_combo["values"] = units
    to_combo["values"] = units

    from_combo.current(0)
    to_combo.current(1)


# ==========================
# GUI
# ==========================

root = tk.Tk()

root.title("Unit Converter Tool")
root.geometry("500x450")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Unit Converter Tool",
    font=("Arial", 20, "bold")
)

title.pack(pady=20)

# Category

tk.Label(
    root,
    text="Select Category"
).pack()

category_var = tk.StringVar()

category_combo = ttk.Combobox(
    root,
    textvariable=category_var,
    state="readonly"
)

category_combo["values"] = (
    "Length",
    "Weight",
    "Temperature"
)

category_combo.pack(pady=5)
category_combo.current(0)
category_combo.bind(
    "<<ComboboxSelected>>",
    update_units
)

# Value

tk.Label(
    root,
    text="Enter Value"
).pack()

entry_value = tk.Entry(root)
entry_value.pack(pady=5)

# From

tk.Label(
    root,
    text="From Unit"
).pack()

from_var = tk.StringVar()

from_combo = ttk.Combobox(
    root,
    textvariable=from_var,
    state="readonly"
)

from_combo.pack(pady=5)

# To

tk.Label(
    root,
    text="To Unit"
).pack()

to_var = tk.StringVar()

to_combo = ttk.Combobox(
    root,
    textvariable=to_var,
    state="readonly"
)

to_combo.pack(pady=5)

# Convert Button

convert_btn = tk.Button(
    root,
    text="Convert",
    command=convert,
    bg="blue",
    fg="white",
    width=20
)

convert_btn.pack(pady=20)

# Result

result_label = tk.Label(
    root,
    text="Result:",
    font=("Arial", 14, "bold")
)

result_label.pack()

update_units()

root.mainloop()