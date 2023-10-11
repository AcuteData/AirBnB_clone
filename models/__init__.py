#!/usr/bin/python3
"""
Initialize the models package
"""

from os import getenv

# Import the necessary storage classes
from models.db_storage import DBStorage
from models.file_storage import FileStorage

# Check the value of the HBNB_TYPE_STORAGE environment variable
storage_t = getenv("HBNB_TYPE_STORAGE")

# Initialize the appropriate storage based on the value of HBNB_TYPE_STORAGE
if storage_t == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

# Call the reload method on the storage instance
storage.reload()
