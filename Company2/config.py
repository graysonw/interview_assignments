import os
import tenacity

friendly = {"url": "http://de-tech-challenge-api.herokuapp.com/api/v1/users"}

company2_mysql = {'host': os.environ.get("MYSQL_HOST"),
         'user': os.environ.get("MYSQL_USER"),
         'password': os.environ.get("MYSQL_PASSWORD"),
         'database': "data_engineer",
         'port': 3316}

dw_mysql = {
'host': "localhost",
         'user': "root",
         'database': "data_warehouse",
         'port': 3306
}


etl_retry_settings = {"wait":tenacity.wait_exponential(multiplier=1, min=4, max=10)}
        #"wait_exponential_multiplier":1000, "wait_exponential_max":10000, "stop_max_delay":30000}
#friendly_retry_settings = {"wait_exponential_multiplier":1000, "wait_exponential_max":10000, "stop_max_delay":30000}

friendly_retry_settings = {"wait":tenacity.wait_exponential(multiplier=1, min=4, max=10)}
