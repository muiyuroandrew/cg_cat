
import os
import json
import pandas as pd

# Define the directory containing the JSONL files and the output directory
data_directory = "C:/Users/andym_000/PycharmProjects/cg_cat/data"
output_directory = "C:/Users/andym_000/PycharmProjects/cg_cat/excel"

# Create the output directory if it doesn't exist
#os.makedirs(output_directory, exist_ok=True)

# Initialize an empty DataFrame to store the combined data
combined_df = pd.DataFrame(columns=["id", "utt", "annot_utt"])

# Iterate through each JSONL file in the data directory
for filename in os.listdir(data_directory):
    if filename.endswith(".jsonl"):
        language_id = os.path.splitext(filename)[0]

        # Read the JSONL file line by line
        with open(os.path.join(data_directory, filename), "r", encoding="utf-8") as file:
            lines = file.readlines()

        # Parse each JSON line and append it to a list
        data_to_append = []
        for line in lines:
            data = json.loads(line)
            data_to_append.append({"id": language_id, "utt": data["utt"], "annot_utt": data["annot_utt"]})

        # Convert the list of dictionaries to a DataFrame and concatenate it with combined_df
        combined_df = pd.concat([combined_df, pd.DataFrame(data_to_append)], ignore_index=True)

# Create an Excel writer object to write multiple sheets
excel_writer = pd.ExcelWriter(f"{output_directory}/en-xx.xlsx", engine="openpyxl")

# Iterate through each unique language id
unique_language_ids = combined_df["id"].unique()
for language_id in unique_language_ids:
    # Create a new DataFrame for each language
    language_df = combined_df[combined_df["id"] == language_id]

    # Write the DataFrame to a new sheet in the Excel file
    language_df.to_excel(excel_writer, sheet_name=f"en-{language_id}", index=False)

# Save the Excel file
excel_writer.save()

# Close the Excel writer
excel_writer.close()
