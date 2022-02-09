import os
from dotenv import dotenv_values

config = {
    **dotenv_values(".env"),  # load sensitive variables
    **os.environ,  # override loaded values with environment variables
}

class DBconfig:
    host = config.get("HOST")
    username = config.get('USERNAME')
    password = config.get('PASSWORD')
