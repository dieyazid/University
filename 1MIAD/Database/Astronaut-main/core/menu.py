from rich.console import Console
from core.tables_manipulation import *
import core.tables_manipulation as tbm
from pick import pick

console = Console()
# Menu's Elements
Main_Menu_Items=['Manage Astronauts','Manage Messions','Exit']
Astronaut_Menu_Items=['View Astronauts','Add Astronaut','Remove Astronaut','Update Astronaut Informations','Home Menu']
Mission_Menu_Items=['View Missions','Add Mission','Add Astronaut to Mission','Remove Mission','Show Astronaut in Mission','Update Mission Details','Home Menu']

def Menu(options,title=''):
    option, index = pick(options, title, indicator='=>', default_index=0)
    return index


def Main_Menu():
    index=Menu(Main_Menu_Items)
    match(index):
        case 0:
            Astronaut_Menu()
        case 1:
            Mission_Menu()
        case _:
            db.connection.commit()
            exit()

def Astronaut_Menu():
    index=Menu(Astronaut_Menu_Items,'##Astronauts Management##')
    match(index):
        case 0:
            Show_Table('SELECT astro_id,first_name,last_name,birthdate,country FROM astronaut',None,tbm.Astronaut_Fields)
        case 1:
            Add_Astronaut()
        case 2:
            Remove_Astronaut()
        case 3:
            Update_Astronaut()
        case _:
            Main_Menu()

def Mission_Menu():
    index=Menu(Mission_Menu_Items,'##Messions Management##')
    match(index):
        case 0:
            Show_Table('SELECT miss_id, miss_name, start_date, end_date, destination FROM mission',None,tbm.Mission_Fields1)
            # Show_Table('SELECT miss_id, miss_name, start_date, end_date, destination, T.first_name,T.last_name FROM mission,TABLE(astronauts_list)T',None,tbm.Mission_Fields1)

        case 1:
            Add_Mission()
        case 2:
            Add_Astro_Mission()
        case 3:
            Remove_Mission()
        case 4:
            Show_Table('SELECT miss_id, miss_name,destination,T.first_name,T.last_name FROM mission,TABLE(astronauts_list)T',None,tbm.Mission_Fields2)
        case 5:
            Update_Mission()
        case _:
            Main_Menu()

# Astronaut Redirect
# def Add_Astro():
#      while True:
#         # id = input('Type The ID of the astronaut : ')
#         # fname = input('Type The First Name of the astronaut : ')
#         # lname = input('Type The Last Name of the astronaut : ')
#         # birthdate = input('Type The Birthdate of the astronaut : ')
#         # country = input('Type The Country of the astronaut : ')
#         id=3
#         fname='Mohamed'
#         lname='Hassan'
#         birthdate='01/01/1999'
#         country='Egypt'
#         # imagepath = filedialog.askopenfilename(filetypes=[("Image File",'.jpg .png .jpeg')])
#         # Load the image file
#         # with open("images/image.jpg", "rb") as image_file:
#         #     image = image_file.read()
#         Confirm_Menu()

   
# Mission Redirect
# def Show_Miss():
#     Show_Table('SELECT miss_id, miss_name, start_date, end_date, destination, T.first_name,T.last_name FROM mission,TABLE(astronauts_list)T',None,dbm.Mission_Fields)
# def Add_Miss():
#     Add_Mission(1,'Mars','01/01/2020','01/01/2021','USA','USA','NULL')
# def Remove_Miss():
#     Remove_Mission()
# def Update_Miss():
#     Update_Mission(1,'Mars','01/01/2020','01/01/2021','USA','USA')
