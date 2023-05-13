import core.Assets.rich as rich
import core.database as db
from core.database import *
from core.tables_manipulation import * 
from core.submenu import Confirm_Menu
from tkinter import filedialog
from prettytable import PrettyTable

Astronaut_Fields=["ID", "First Name", "Last Name", "Birthdate", "Country"]
Mission_Fields1=["ID", "Mission name", "Launch date", "Arrive Date", "Destination"]
Mission_Fields2=["ID", "Mission name", "Destination","ASTRONAUT FIRST NAME","ASTRONAUT LAST NAME"]


def Show_Table(statement: str , values: list | tuple | dict = None , fields: list=[], **keyword_parameters: dict):
    # Execute the SELECT statement
    db.cursor.execute(statement,values)
    # Fetch the rows
    rows = db.cursor.fetchall()
    # print(rows)
    # Check if the result is empty
    if len(rows) == 0:
        rich.console.print("[yellow]No rows returned[/]")
        return False
    else:
        # Create a PrettyTable
        table = PrettyTable()
        # Add the column names
        table.field_names = fields
        # Add the rows to the table
        for row in rows:
            table.add_row(row)
        # Print the table
        print(table)
        return True

# Astronaut Table Operations
def Add_Astronaut():
    while True:
        id = input('Type The ID of the astronaut : ')
        fname = input('Type The First Name of the astronaut : ')
        lname = input('Type The Last Name of the astronaut : ')
        birthdate = input('Type The Birthdate of the astronaut : ')
        country = input('Type The Country of the astronaut : ')
        imagepath = filedialog.askopenfilename(filetypes=[("Image File",'.jpg .png .jpeg')])
        # Load the image file
        with open(imagepath, "rb") as image_file:
            id_photo = image_file.read()
        decision=Confirm_Menu('Are you sure?(y/n/cancel)')
        if decision == True:
            insert_statement = """
            INSERT INTO astronaut
            VALUES (:astro_id, :first_name, :last_name, TO_DATE(:birthdate,'dd/mm/yyyy'), :country, :id_photo)
            """
            # Define the values to insert
            values = {
                "astro_id": id,
                "first_name": fname,
                "last_name": lname,
                "birthdate": birthdate,
                "country": country,
                "id_photo": id_photo
            }
            # Execute the INSERT statement
            try:
                execute_command(insert_statement, values)
                
            except oracledb.Error as error:
                print(error)
                pass
            break
        elif decision == False:
            pass
        elif decision == None:
            break

def Remove_Astronaut():
    while True:
        user_input = input('Type The First Name Or Last Name Or ID of the astronaut : ')
        statement= '''SELECT * FROM astronaut WHERE astro_id= :id OR first_name= :fname OR last_name= :lname '''
        if user_input.isdigit():
            values = {
                "id": user_input,
                "fname": None,
                "lname": None
            }
        else:
            values = {
                "id": None,
                "fname": user_input,
                "lname": user_input
            }
        rows_state=Show_Table(statement,values,Astronaut_Fields)
        if rows_state:
            decision=Confirm_Menu('You cannot undo this operation! Are you sure?(y/n/cancel)')
            if decision == True:
                execute_command(f'''
                DELETE FROM astronaut
                WHERE astro_id = :id OR first_name = :fname OR last_name = :lname
                ''',values)
                break
            elif decision == False:
                pass
            elif decision == None:
                break
        else:
            rich.console.print('[red]User Not Found![/]')
            if Confirm_Menu('Do you want to continue?(y,n)'):
                pass
            else:
                break

def Update_Astronaut():
    pass



# Mission Table Operations
def Add_Mission():
    while True:
        # miss_id = input('Type Mission ID : ')
        # miss_name = input('Type Mission Name : ')
        # start_date= input('Type Mission Start Date :')
        # end_date = input('Type Mission End Date : ')
        # destination = input('Type Destination : ')
        miss_id=1
        miss_name='APOLO'
        start_date='05/06/2022'
        end_date='03/05/2025'
        destination='Moon'
        decision=Confirm_Menu('Are you sure?(y/n/cancel)')
        if decision == True:
            # Define the INSERT statement
            insert_statement = """
            INSERT INTO mission(miss_id, miss_name, start_date, end_date, destination,astronauts_list)
            VALUES (:miss_id, :miss_name, TO_DATE(:start_date,'DD/MM/YYYY'), TO_DATE(:end_date,'MM/DD/YYYY'), :destination,NULL)
            """
            # Define the values to insert
            values = {
                "miss_id": miss_id,
                "miss_name": miss_name,
                "start_date": start_date,
                "end_date": end_date,
                "destination": destination
            }
            # Execute the INSERT statement
            try:
                execute_command(insert_statement, values)
            except oracledb.Error as error:
                print(error)
                pass
            break
        elif decision == False:
            pass
        elif decision == None:
            break

def Remove_Mission():
    while True:
        user_input = input('Type The Mission Name Or ID of the astronaut : ')
        statement='''SELECT miss_id, miss_name, start_date, end_date, destination FROM mission WHERE miss_id= :id OR miss_name= :mname'''
        if user_input.isdigit():
            values = {
                "id": user_input,
                "mname": None
            }
        else:
            values = {
                "id": None,
                "mname": user_input
            }
        rows_state=Show_Table(statement,values,Mission_Fields2)
        # Show_Table('statement',None,dbm.Astronaut_Fields)
        if rows_state:
            decision=Confirm_Menu('You cannot undo this operation! Are you sure?(y/n/cancel)')
            if decision == True:
                execute_command(f'''
                DELETE FROM mission
                WHERE miss_id = :id OR miss_name = :mname
                ''',values)
                break
            elif decision == False:
                pass
            elif decision == None:
                break
        else:
            rich.console.print('[red]Mission Not Found![/]')
            if Confirm_Menu('Do you want to continue?(y,n)'):
                pass
            else:
                break
def Update_Mission():
    pass

def Add_Astro_Mission():
    pass


