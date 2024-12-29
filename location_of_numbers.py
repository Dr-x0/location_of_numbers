import phonenumbers
from phonenumbers import geocoder, carrier
import tkinter as tk
from tkinter import messagebox
from opencage.geocoder import OpenCageGeocode

def show_location():
    enter_num = entry.get()
    try:
        phone = phonenumbers.parse(enter_num)
        if not phonenumbers.is_valid_number(phone):
            messagebox.showerror("Error", "Invalid phone number.")
        else:
            number_location = geocoder.description_for_number(phone, "en")
            service_provider = carrier.name_for_number(phone, "en")
            
            geocoder_api = OpenCageGeocode('YOUR_API_KEY')
            query = str(number_location)
            results = geocoder_api.geocode(query)

            if results:
                lat = results[0]['geometry']['lat']
                lng = results[0]['geometry']['lng']
                location_label.config(text=f"Location: {lat}, {lng}")
                map_button.config(state="normal")  # Enable map button
            else:
                messagebox.showerror("Error", "Location not found.")
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred: {str(e)}")

root = tk.Tk()
root.title("Phone Location Tracker")
root.geometry("400x300")
root.configure(bg="#2C3E50")  # Background color

# Entry for phone number
entry_label = tk.Label(root, text="Enter Phone Number:", font=("Helvetica", 12), bg="#2C3E50", fg="#ECF0F1")
entry_label.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 12), bg="#34495E", fg="#ECF0F1", insertbackground="white", width=20)
entry.pack(pady=10)

# Location display
location_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#2C3E50", fg="#ECF0F1")
location_label.pack(pady=10)

# Buttons
search_button = tk.Button(root, text="Show Location", font=("Helvetica", 12), bg="#1ABC9C", fg="#ECF0F1", command=show_location)
search_button.pack(pady=10)

map_button = tk.Button(root, text="View Map", font=("Helvetica", 12), bg="#E67E22", fg="#ECF0F1", state="disabled")
map_button.pack(pady=10)

root.mainloop()
