from helpers.env_helper import EnvironmentHandler
from .sq_lite import SQLiteConnection
from .queries import table_queries
from .db_tables import Tables as TABLE_NAMES

db_name = 'library.db' if EnvironmentHandler.get_env_variable('DB_NAME') is None else EnvironmentHandler.get_env_variable('DB_NAME')
con_retry_number = 5 if EnvironmentHandler.get_env_variable('RETRIES') is None else int(EnvironmentHandler.get_env_variable('RETRIES'))

connection = SQLiteConnection(db_name, max_retries=con_retry_number)


def create_initial_db_with_tables():
    try:
        with SQLiteConnection(db_name, con_retry_number) as con:
            cursor = con.cursor()

            for query_name, query in table_queries.items():
                cursor.execute(query)

    except Exception as e:
        print('Error: create_initial_db_with_tables:', e)
