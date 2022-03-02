import os
from dotenv import dotenv_values

config = {
    **dotenv_values(".env"),  # load sensitive variables
}

class DBconfig:
    host = config.get("HOST")
    username = config.get('USERNAME')
    password = config.get('PASSWORD')
