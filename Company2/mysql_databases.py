import mysql.connector
import logging
from tenacity import retry

import queries
import config

# We use this class that both the Company2 database and the
# data warehouse inherit from.
class Database:
    @retry(**config.etl_retry_settings)
    def __init__(self, db_config):
        self.connection = mysql.connector.connect(**db_config)
        self.cursor = self.connection.cursor(dictionary=True)

    def __del__(self):
        if self.connection.is_connected():
            self.connection.close()
            self.cursor.close()


class Company2(Database):
    @retry(**config.etl_retry_settings)
    def get_first_page(self, end_user: dict):
        try:
            self.cursor.execute(queries.get_first_page_query,
                                (end_user["lastname"], end_user["lastname"], end_user["firstname"]))
            return [row for row in self.cursor]
        except Exception as e:
            logging.error(e)

    @retry(**config.etl_retry_settings)
    def get_middle_page(self, start_user: dict, end_user: dict):
        self.cursor.execute(queries.get_middle_page_query,
                                (start_user["lastname"], end_user["lastname"],
                                 start_user["lastname"], start_user["firstname"],
                                 end_user["lastname"], end_user["firstname"]))

        return [row for row in self.cursor]

    @retry(**config.etl_retry_settings)
    def get_last_page(self, start_user: dict):
        self.cursor.execute(queries.get_last_page_query,
                                (start_user["lastname"],
                                 start_user["lastname"],
                                 start_user["firstname"]))

        return [row for row in self.cursor]


class DW(Database):
    @retry(**config.etl_retry_settings)
    def __init__(self, config):
        super().__init__(config)
        logging.info(queries.create_table_query)

        # We create the table, and truncate it if there's anything in it. I
        # mostly added this so I could run this code repeatedly and not have to
        # truncate it manually each time--in production this would of course be 
        # different and we'd have incremental loads.
        self.cursor.execute(queries.create_table_query)
        self.cursor.execute("TRUNCATE TABLE usermatching;")

    @retry(**config.etl_retry_settings)
    def insert(self, data):
        try:
            self.cursor.executemany(queries.insert_table_query, data)
            self.connection.commit()
        except Exception as e:
            logging.error(e)
            self.connection.rollback()
            raise Exception
