# /usr/bin/python3
import os

# Define the documentation to be inserted
documentation = '''
"""
Module Documentation for {filename}:

{description}
"""
'''

# Function to wrap text to a maximum line length
def wrap_text(text, line_length=79):
    words = text.split()
    lines = []
    current_line = ''
    for word in words:
        if len(current_line) + len(word) <= line_length:
            current_line += word + ' '
        else:
            lines.append(current_line.rstrip())
            current_line = word + ' '
    if current_line:
        lines.append(current_line.rstrip())
    return '\n'.join(lines)

# Define the descriptions for each file
descriptions = {
    "0-select_states.py": "This module contains a Python script that interacts with a MySQL database using MySQLdb. It fetches all rows from the 'states' table in the specified database and prints them.",
    "1-filter_states.py": "This module contains a Python script that interacts with a MySQL database using SQLAlchemy ORM. It fetches states with names starting with 'N' from the 'states' table in the specified database.",
    "2-my_filter_states.py": "This module contains a Python script that interacts with a MySQL database using MySQLdb. It fetches a state with a specific name from the 'states' table in the specified database.",
    "3-my_safe_filter_states.py": "This module contains a Python script that interacts with a MySQL database using MySQLdb. It fetches a state with a specific name from the 'states' table in the specified database using a parameterized query.",
    "4-cities_by_state.py": "This module contains a Python script that interacts with a MySQL database using SQLAlchemy ORM. It retrieves city names from cities in a state specified by name from the 'cities' and 'states' tables in the specified database.",
    "5-filter_cities.py": "This module contains a Python script that interacts with a MySQL database using SQLAlchemy ORM. It deletes states with names containing 'a' from the 'states' table in the specified database.",
    "6-model_state.py": "This module defines the State class using SQLAlchemy ORM for mapping to the 'states' table in the database.",
    "7-model_state_fetch_all.py": "This module contains a Python script that interacts with a MySQL database using SQLAlchemy ORM. It retrieves all states from the 'states' table in the specified database and prints their IDs and names.",
    "8-model_state_fetch_first.py": "This module contains a Python script that interacts with a MySQL database using SQLAlchemy ORM. It retrieves the first state from the 'states' table in the specified database and prints its ID and name.",
    "9-model_state_filter_a.py": "This module contains a Python script that interacts with a MySQL database using SQLAlchemy ORM. It retrieves states with names containing 'a' from the 'states' table in the specified database and prints their IDs and names.",
    "10-model_state_my_get.py": "This module contains a Python script that interacts with a MySQL database using SQLAlchemy ORM. It retrieves a state with a specific name from the 'states' table in the specified database using a custom get method.",
    "11-model_state_insert.py": "This module contains a Python script that interacts with a MySQL database using SQLAlchemy ORM. It inserts a new state into the 'states' table in the specified database.",
    "12-model_state_update_id_2.py": "This module contains a Python script that interacts with a MySQL database using SQLAlchemy ORM. It updates the name of a state in the 'states' table in the specified database.",
    "13-model_state_delete_a.py": "This module contains a Python script that interacts with a MySQL database using SQLAlchemy ORM. It deletes states with names containing 'a' from the 'states' table in the specified database.",
    "14-model_city_fetch_by_state.py": "This module contains a Python script that interacts with a MySQL database using SQLAlchemy ORM. It retrieves city names along with their corresponding state names from the 'cities' and 'states' tables in the specified database.",
    "model_state.py": "This module defines the State class using SQLAlchemy ORM for mapping to the 'states' table in the database.",
    "model_city.py": "This module defines the City class using SQLAlchemy ORM for mapping to the 'cities' table in the database.",
}

# Iterate through each file and insert the documentation
# Iterate through each file and insert the documentation
for filename, description in descriptions.items():
    wrapped_description = wrap_text(description)
    file_path = os.path.join(".", filename)
    with open(file_path, "r+") as file:
        content = file.readlines()
        content.insert(1, documentation.format(filename=filename, description=wrapped_description) + "\n")
        file.seek(0)
        file.writelines(content)
