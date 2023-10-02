
import os
import json
from googletrans import Translator

# Define the directory containing the JSONL files, the output JSON file, and the target languages
data_directory = "C:/Users/andym_000/PycharmProjects/cg_cat/data"
output_json_file = "C:/Users/andym_000/PycharmProjects/cg_cat/output"
target_languages = ["fr", "es", "de"]  # Add the languagesy needed

# Initialize an empty dictionary to store the translations
translations = {}

# Create a Translator instance
translator = Translator()

# Iterate through each JSONL file in the data directory
for filename in os.listdir(data_directory):
    if filename.endswith(".jsonl"):
        language_id = os.path.splitext(filename)[0]
        language_translations = []

        # Read the JSONL file line by line
        with open(os.path.join(data_directory, filename), "r", encoding="utf-8") as file:
            lines = file.readlines()

        # Parse each JSON line and extract and generate translations
        for line in lines:
            data = json.loads(line)
            en_translation = data.get("utt")

            if en_translation:
                language_translation_entry = {"id": language_id, "en": en_translation}

                # Generate translations for each target language
                for target_language in target_languages:
                    translated = translator.translate(en_translation, src="en", dest=target_language)
                    language_translation_entry[target_language] = translated.text

                language_translations.append(language_translation_entry)

        # Add the translations for this language to the dictionary
        translations[language_id] = language_translations

# Write the combined translations to a single JSON file
with open(output_json_file, "w", encoding="utf-8") as json_file:
    json.dump(translations, json_file, ensure_ascii=False, indent=4)
