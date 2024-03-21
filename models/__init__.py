#!/usr/bin/python3
"""Initializes the models package."""
from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance
storage = FileStorage()
# Call reload() method on the storage variable
storage.reload()
