import json
import os

# Define the directory where your JSON files are located
data_directory = '../data'

# List of languages and corresponding file names
languages = ['en', 'sw', 'de']
file_names = ['data_en.json', 'data_sw.json', 'data_de.json']

# Create a dictionary to store the data for each language
data_by_language = {}

for language, file_name in zip(languages, file_names):
    file_path = os.path.join(data_directory, file_name)

    # Check if the file exists
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Store the data in the dictionary with the language as the key
        data_by_language[language] = data
    else:
        print(f"File not found for language: {language}")

# Now you have the data organized by language in the 'data_by_language' dictionary
# For example, to access English data:
english_data = data_by_language.get('en', [])

# To access Swahili data:
swahili_data = data_by_language.get('sw', [])

# To access German data:
german_data = data_by_language.get('de', [])

# You can now work with the data as needed
