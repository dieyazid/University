import oracledb
import core.Assets.rich as rich
import configparser

cursor = oracledb.Cursor
# connection = oracledb.Connection
#note: cursor is empty before connecting to the database 
def connect_to_database(config_file):
    global cursor,connection
    rich.console.print("[cyan]Connecting to Oracle Database please be patient...[/]")
    config = configparser.ConfigParser()
    config.read(config_file)

    username = config['DEFAULT']['username']
    password = config['DEFAULT']['password']
    host = config['DEFAULT']['host']
    try:
        connection = oracledb.connect(
        user=username,
        password=password,
        dsn=host)
        rich.console.print("[bold][green]Successfully connected to Oracle Database[/]")
    except oracledb.Error as error:
        rich.console.print(f"[bold][red]Error connecting to the database: [/][/]\n{error}")
        exit()
    cursor = connection.cursor()
    connection = connection
    return connection

# def excute_command(*args,**kwargs)
def execute_command(statement: str | None, parameters: list | tuple | dict = None, **keyword_parameters: dict):
    try:
        cursor.execute(statement, parameters, **keyword_parameters)
        rich.console.print("[bold][green]Operation Done![/]")
    except oracledb.Error as error:
        rich.console.print(f'[red]{error}[/]')
        pass

def Fetch_All():
    try:
        return cursor.fetchall()
    except oracledb.Error as error:
        rich.console.print(f'[red]{error}[/]')
        return []

def run_sql_script(script_path):
    statement_parts = []
    for line in open(script_path):
        if line.strip() == "@":
            statement = "".join(statement_parts).strip()
            if not statement.upper().startswith('CREATE PACKAGE'):
                statement = statement[:-1]
            if statement:
                try:
                    cursor.execute(statement)
                    # console.print(f'[green]{statement.split(" ")[0]} {statement.split(" ")[2]} successful![/]')
                except Exception as error:
                    rich.console.print(f'[red]{error}[/]')
            statement_parts = []
        else:
            statement_parts.append(line)