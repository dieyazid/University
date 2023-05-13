from core.database import *
from core.menu import *
from core.database_setup import *

# Connect to database 
connection = connect_to_database('core/config.ini')
# Create Database Elements
Drop_All()
print("###############")
Create_database_elements()


# Main Loop
while True:
    Main_Menu()
    input('Press Any Key to continue!')
    db.connection.commit()