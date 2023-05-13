from core.database import *

def Create_database_elements():
    run_sql_script("sql/setup.sql")
    # run_sql_script("sql/trigger.sql")
    # run_sql_script("sql/insert.sql")

def Drop_All():
    run_sql_script("sql/drop.sql")
