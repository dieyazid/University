import cx_Oracle
from tkinter import filedialog
from PIL import Image
import io


# Connect to the database
try:
    connection = cx_Oracle.connect('astronaut',
    'password',
    'localhost/XEPDB1')
    print("Connected")
except cx_Oracle.Error as error:
    print("Error")

# Create a cursor
cursor = connection.cursor()
# cursor.execute('''DROP TABLE images''')
# cursor.execute('''CREATE TABLE images (id INT PRIMARY KEY,image BLOB)''')
imagepath = filedialog.askopenfilename(filetypes=[("Image File",'.jpg .png .jpeg')])

# Load the image file
with open(imagepath, "rb") as image_file:
    image = image_file.read()

try:
# Insert the image into the database
    cursor.execute("INSERT INTO images (id, image) VALUES (1, :image)", image=image)
except cx_Oracle.DatabaseError as error:
    pass
# Commit the changes
connection.commit()

# Select the image from the database
cursor.execute("SELECT image FROM images WHERE id = 1")
image_from_database = cursor.fetchone()[0]

# Convert the LOB object to a bytes object
image_bytes = image_from_database.read()

print(type(image_bytes))
# Open the image file
image = Image.open(io.BytesIO(image_bytes))

# Show the image in a window
image.show()

# # Save the image to a file
# with open("image_from_database.jpg", "wb") as image_file:
#     image_file.write(image_bytes)

cursor.execute('''DROP TABLE images''')
connection.commit()
# Close the cursor and connection
cursor.close()
connection.close()
