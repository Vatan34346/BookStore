from .i_base_sql_service import ISQLService
from database import connection
import sqlite3


class SQLService(ISQLService):
    """
    dev: panteleimon gvichia
    description: class that operates with db, Making crud operation on any table.
    phone: +7995123456
    """
    def __init__(self):
        self.connection = connection

    def insert_data(self, table_name, data):
        try:
            with self.connection as conn:
                cursor = conn.cursor()
                columns = ', '.join(data.keys())
                placeholders = ', '.join(['?' for _ in data.values()])
                query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                cursor.execute(query, tuple(data.values()))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            print('Sqlite Error(SQLService) insert_data:', e)
            return None
        except Exception as e:
            print('Error(SQLService) insert_data:', e)
            return None

    def get_data(self, table_name, fields=None, filters=None):
        try:
            with self.connection as conn:
                cursor = conn.cursor()
                if fields is None:
                    field_list = '*'
                else:
                    field_list = ', '.join(fields)

                query = f"SELECT {field_list} FROM {table_name}"

                filter_conditions = []
                filter_values = []

                if filters:
                    for column, value in filters.items():
                        filter_conditions.append(f"{column} = ?")
                        filter_values.append(value)

                    query += f" WHERE {' AND '.join(filter_conditions)}"

                cursor.execute(query, tuple(filter_values))
                rows = cursor.fetchall()

                # columns
                column_names = [desc[0] for desc in cursor.description]

                data = []
                for row in rows:
                    row_dict = dict(zip(column_names, row))

                    # is foreign key
                    for column, value in row_dict.items():
                        if column.endswith('_id'):
                            # delete _id col name
                            related_table_name = column[:-3]
                            related_data = self.get_data(
                                table_name=related_table_name,
                                fields=['*'],
                                filters={'id': value}
                            )
                            row_dict[column] = related_data  # Store related data as a list

                    data.append(row_dict)
                return data

        except sqlite3.Error as e:
            print("Sqlite Error(SQLService) get_data:", e)
            return None
        except Exception as e:
            print('Error(SQLService) get_data:', e)
            return None

    def delete_object(self, table_name, _id):
        try:
            with self.connection as conn:
                cursor = conn.cursor()
                query = f"DELETE FROM {table_name} WHERE id = ?"
                cursor.execute(query, (_id,))
                conn.commit()
                return cursor.rowcount > 0

        except sqlite3.Error as e:
            print('Sqlite Error(SQLService) delete_object:', e)
            return False
        except Exception as e:
            print('Error(SQLService) delete_object:', e)
            return False

    def update_object(self, table_name, _id, new_data):
        try:
            with self.connection as conn:
                cursor = conn.cursor()

                set_clause = ', '.join([f"{column} = ?" for column in new_data.keys()])

                query = f"UPDATE {table_name} SET {set_clause} WHERE id = ?"  # Assuming 'id' is the primary key

                query_values = tuple(list(new_data.values()) + [_id])

                cursor.execute(query, query_values)
                conn.commit()
                return cursor.rowcount > 0

        except sqlite3.Error as e:
            print('Sqlite Error(SQLService) update_object:', e)
            return False
        except Exception as e:
            print('Error(SQLService) update_object:', e)
            return False

    def get_object_by_(self, table_name, field_name, field_value):
        try:
            with self.connection as conn:
                cursor = conn.cursor()
                query = f"SELECT * FROM {table_name} WHERE {field_name} = ?"  # Assuming 'id' is the primary key
                cursor.execute(query, (field_value,))
                row = cursor.fetchone()

                if row:
                    column_names = [desc[0] for desc in cursor.description]

                    object_data = dict(zip(column_names, row))

                    return object_data

        except sqlite3.Error as e:
            print('Sqlite Error(SQLService) get_object_by_id:', e)
            return None
        except Exception as e:
            print('Error(SQLService) get_object_by_id:', e)
            return None
