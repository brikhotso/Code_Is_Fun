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
    "0-script.py": "add documentation here.",
    "1-script.py": "add documentation here.",
    "2-script.py": "add documentation here.",
    "3-script.py": "add documentation here.",
    "4-script.py": "add documentation here.",
    "5-script.py": "add documentation here.",
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
