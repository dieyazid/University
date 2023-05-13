import tkinter as tk

from core.database import *
from core.menu import *
from core.database_setup import *

# Connect to database 
cnx = connect_to_database('core/config.ini')
# cursor = cnx.cursor()

# Create the main window
window = tk.Tk()
window.title("Update Table")

# Create the label and entry for the astronaut ID
astro_id_label = tk.Label(window, text="Astronaut ID:")
astro_id_label.grid(row=0, column=0)
astro_id_entry = tk.Entry(window)
astro_id_entry.grid(row=0, column=1)

# Create the label and entry for the first name
first_name_label = tk.Label(window, text="First Name:")
first_name_label.grid(row=1, column=0)
first_name_entry = tk.Entry(window)
first_name_entry.grid(row=1, column=1)

# Create the label and entry for the last name
last_name_label = tk.Label(window, text="Last Name:")
last_name_label.grid(row=2, column=0)
last_name_entry = tk.Entry(window)
last_name_entry.grid(row=2, column=1)

# Create the label and entry for the birthdate
birthdate_label = tk.Label(window, text="Birthdate:")
birthdate_label.grid(row=3, column=0)
birthdate_entry = tk.Entry(window)
birthdate_entry.grid(row=3, column=1)

# Create the label and entry for the country
country_label = tk.Label(window, text="Country:")
country_label.grid(row=4, column=0)
country_entry = tk.Entry(window)
country_entry.grid(row=4, column=1)

# Create the label and entry for the ID photo
id_photo_label = tk.Label(window, text="ID Photo:")
id_photo_label.grid(row=5, column=0)
id_photo_entry = tk.Entry(window)
id_photo_entry.grid(row=5, column=1)

# Create the update button
def update_button_clicked():
    # Get the values from the entries
    astro_id = astro_id_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    birthdate = birthdate_entry.get()
    country = country_entry.get()
    id_photo = id_photo_entry.get()

    # Construct the update statement
    update_stmt = f"UPDATE astronaut SET first_name= :first_name, last_name= :last_name, birthdate= birthdate, country= :country, id_photo= :id_photo WHERE astro_id= :astro_id"
    values = {
                "astro_id": astro_id,
                "first_name": first_name,
                "last_name": last_name,
                "birthdate": birthdate,
                "country": country,
                "id_photo": id_photo
            }
    # Execute the update statement
    cursor.execute(update_stmt,values)
    cnx.commit()

    # Clear the entries
    astro_id_entry.delete(0, tk.END)
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    birthdate_entry.delete(0, tk.END)
    country_entry.delete(0, tk.END)
    id_photo_entry.delete(0, tk.END)

update_button = tk.Button(window, text="Update", command=update_button_clicked)
update_button.grid(row=6, column=0, columnspan=2)

# Run the main loop
window.mainloop()

# Close the cursor and connection
cursor.close()
cnx.close()

