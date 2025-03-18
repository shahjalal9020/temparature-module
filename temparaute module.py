import tkinter as tk
from tkinter import ttk

# Conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

# Function to perform conversion
def convert_temperature():
    try:
        input_temp = float(entry.get())  # Get input temperature
        input_scale = input_combobox.get()  # Get input scale
        output_scale = output_combobox.get()  # Get output scale

        # Convert input to Celsius first (if needed)
        if input_scale == "Celsius":
            celsius = input_temp
        elif input_scale == "Fahrenheit":
            celsius = fahrenheit_to_celsius(input_temp)
        elif input_scale == "Kelvin":
            celsius = kelvin_to_celsius(input_temp)

        # Convert Celsius to the desired output scale
        if output_scale == "Celsius":
            result = celsius
        elif output_scale == "Fahrenheit":
            result = celsius_to_fahrenheit(celsius)
        elif output_scale == "Kelvin":
            result = celsius_to_kelvin(celsius)

        # Display the result
        result_label.config(text=f"Result: {result:.2f} {output_scale}")
    except ValueError:
        result_label.config(text="Invalid input! Please enter a number.")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x300")

# Input temperature entry
entry_label = tk.Label(root, text="Enter Temperature:")
entry_label.pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

# Input scale selection
input_label = tk.Label(root, text="From:")
input_label.pack(pady=5)
input_combobox = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"])
input_combobox.pack(pady=5)
input_combobox.set("Celsius")  # Default value

# Output scale selection
output_label = tk.Label(root, text="To:")
output_label.pack(pady=5)
output_combobox = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"])
output_combobox.pack(pady=5)
output_combobox.set("Fahrenheit")  # Default value

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack(pady=20)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=10)

# Run the application
root.mainloop()