import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import pandas as pd
from bug_detector import detect_bug
from csv_writer import write_csv


# Load dataset
df = pd.read_csv("C:/Users/chait/Downloads/infineon/samples.csv")

df = df.sort_values("ID").reset_index(drop=True)
print("Dataset loaded")
print("Columns:", df.columns)
print("Total rows:", len(df))

# results = []

# Process each code snippet
# for _, row in df.iterrows():

#     code_id = row["ID"]
#     code = row["Code"]
#     correct_code = row["Correct Code"]

#     print(f"Processing ID: {code_id}")

#     try:
#         bug_line, explanation = detect_bug(code, correct_code)

#         results.append({
#             "ID": code_id,
#             "Bug Line": bug_line,
#             "Explanation": explanation
#         })

#     except Exception as e:
#         print(f"Error processing ID {code_id}: {e}")

#         results.append({
#             "ID": code_id,
#             "Bug Line": "Error",
#             "Explanation": str(e)
#         })

results = []

for i in range(len(df)):

    row = df.iloc[i]

    code_id = row["ID"]
    code = row["Code"]
    correct_code = row["Correct Code"]

    print(f"Processing row {i} | ID {code_id}")

    try:
        bug_line, explanation = detect_bug(code, correct_code)

    except Exception as e:

        print("API error:", e)
        print("Stopping execution safely.")

        break

    results.append({
        "ID": code_id,
        "Bug Line": bug_line,
        "Explanation": explanation
    })

    # save progress every row
    write_csv(results)



# Save results
# write_csv(results)

print("✅ Finished generating output.csv")