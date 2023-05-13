from pick import pick

title = 'Please choose your favorite programming language: '
options = ['Java', 'JavaScript', 'Python', 'PHP', 'C++', 'Erlang', 'Haskell']

option, index = pick(options, title, indicator='=>', default_index=2)

print(option,index)


####################################

import curses
import functools
from rich.console import Console
from core.tables_manipulation import *
from core.mission_manipulation import * 
import core.database_manipulation as dbm

console = Console()
decision=False
# Menu's Elements
Main_Menu_Items=['Manage Astronauts','Manage Messions','Exit']
Astronaut_Menu_Items=['View Astronauts','Add Astronaut','Remove Astronaut','Update Astronaut Informations','Home Menu']
Mission_Menu_Items=['View Missions','Add Mission','Remove Mission','Update Mission Details','Home Menu']
Confirm_Menu_Items=['YES','TRY AGAIN','QUIT']

def To_Menu(_func=None,*,Title=""):
    def DecoratorTo_Menu(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            dic=func(*args, **kwargs)
            options=list(dic.keys())
            functions=list(dic.values())
            index= curses.wrapper(Menu,Title,options)
            functions[index]() 
        return wrapper
    
    if _func is None:
        return DecoratorTo_Menu
    else:
        return DecoratorTo_Menu(_func)


def Menu(stdscr,title,items):
    attributes = {}
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    attributes['normal'] = curses.color_pair(1)

    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    attributes['highlighted'] = curses.color_pair(2)

    c = 0  # last character read
    option = 0  # the current option that is marked
    while c != 10:  # Enter in ascii
        stdscr.erase()
        stdscr.addstr(f"{title}\n", curses.A_UNDERLINE)
        for i in range(len(items)):
            if i == option:
                attr = attributes['highlighted']
            else:
                attr = attributes['normal']
            stdscr.addstr("[{0}] ".format(i + 1))
            stdscr.addstr(items[i] + '\n', attr)
        c = stdscr.getch()
        if c == curses.KEY_UP and option > 0:
            option -= 1
        elif c == curses.KEY_DOWN and option < len(items) - 1:
            option += 1
    return option

@To_Menu
def Main_Menu():
    menu={f" {Main_Menu_Items[0]} ":Astronaut_Menu,
            f" {Main_Menu_Items[1]}":Mission_Menu,
            f"  {Main_Menu_Items[2]}":exit
    }
    return menu


@To_Menu(Title='Astronauts Management')
def Astronaut_Menu():
    menu={f" {Astronaut_Menu_Items[0]}":Show_Astro,
            f" {Astronaut_Menu_Items[1]}":Add_Astro,
            f" {Astronaut_Menu_Items[2]}":Remove_Astro,
            f" {Astronaut_Menu_Items[3]}":Update_Astronaut,
            f" {Astronaut_Menu_Items[4]}":Main_Menu
    }
    return menu

@To_Menu(Title='Messions Management')
def Mission_Menu():
    menu={f" {Mission_Menu_Items[0]}":Show_Miss,
            f" {Mission_Menu_Items[1]}":Add_Miss,
            f" {Mission_Menu_Items[2]}":Remove_Miss,
            f" {Mission_Menu_Items[3]}":Update_Miss,
            f" {Mission_Menu_Items[4]}":Main_Menu
    }
    return menu

@To_Menu(Title='Are you sure?')
def Confirm_Menu():
    menu={f" {Confirm_Menu_Items[0]}":true,
            f" {Confirm_Menu_Items[1]}":false,
            f" {Confirm_Menu_Items[2]}":none
    }
    return menu

# Astronaut Redirect
def Add_Astro():
     while True:
        # id = input('Type The ID of the astronaut : ')
        # fname = input('Type The First Name of the astronaut : ')
        # lname = input('Type The Last Name of the astronaut : ')
        # birthdate = input('Type The Birthdate of the astronaut : ')
        # country = input('Type The Country of the astronaut : ')
        id=3
        fname='Mohamed'
        lname='Hassan'
        birthdate='01/01/1999'
        country='Egypt'
        # imagepath = filedialog.askopenfilename(filetypes=[("Image File",'.jpg .png .jpeg')])
        # Load the image file
        # with open("images/image.jpg", "rb") as image_file:
        #     image = image_file.read()
        Confirm_Menu()
        if decision == True:
            Add_Astronaut(id,fname,lname,birthdate,country)
            pass
        elif decision == False:
            pass
        else:
            exit()

def Show_Astro():
    Show_Table('SELECT * FROM astronaut',None,dbm.Astronaut_Fields)
def Remove_Astro():
    Remove_Astronaut()
def Update_Astronaut():
    pass

   
# Mission Redirect
def Show_Miss():
    Show_Table('SELECT miss_id, miss_name, start_date, end_date, destination, T.first_name,T.last_name FROM mission,TABLE(astronauts_list)T',None,dbm.Mission_Fields)
def Add_Miss():
    Add_Mission(1,'Mars','01/01/2020','01/01/2021','USA','USA','NULL')
def Remove_Miss():
    Remove_Mission()
def Update_Miss():
    Update_Mission(1,'Mars','01/01/2020','01/01/2021','USA','USA')

# Commit and Quit
def quit_():
    db.connection.commit()
    exit()

# Confirmation Menu Decision
def true():
    global decision
    decision=True
def false():
    global decision
    decision= False
def none():
    global decision
    decision= None