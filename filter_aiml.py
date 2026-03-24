import sys
import pandas as pd

input_file = "Industrial Internship (23CSI-338) Data Submission AIT-CSE Batch (2023-2027) (Responses).xlsx"
output_file = "AIML_Internship_Data.xlsx"
specialization_col = "Specialization Programs"
aiml_value = "BE CSE (H) in AIML"

# Read the industrial internship Excel file
try:
    df = pd.read_excel(input_file)
except FileNotFoundError:
    print(f"Error: Input file not found — '{input_file}'")
    print("Please ensure the file is in the current working directory.")
    sys.exit(1)

# Validate that the required column exists
if specialization_col not in df.columns:
    print(f"Error: Expected column '{specialization_col}' not found in the file.")
    print(f"Available columns: {list(df.columns)}")
    sys.exit(1)

# Filter rows where specialisation belongs to AI/ML
aiml_df = df[df[specialization_col] == aiml_value].reset_index(drop=True)

# Save filtered data to a new Excel file
try:
    aiml_df.to_excel(output_file, index=False)
except OSError as e:
    print(f"Error: Could not write output file '{output_file}' — {e}")
    sys.exit(1)

print(f"Total records in original file : {len(df)}")
print(f"AI/ML specialisation records   : {len(aiml_df)}")
print(f"Filtered data saved to         : {output_file}")
