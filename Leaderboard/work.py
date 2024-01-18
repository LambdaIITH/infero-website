import pandas as pd
import json

# Load Excel data into a DataFrame
excel_file = 'data.xlsx'
df = pd.read_excel(excel_file)

# Load JSON data
json_file = 'final.json'
with open(json_file, 'r') as f:
    data = json.load(f)

users_list = data['users']
# Create a new list to store updated user data
updated_users = []
j = 1
# Iterate through each person in the JSON data
for user in users_list:
    handle = user['handle']
    score = user['total']
    # Check if the handle is present in the Excel file
    for i in range(len(df)-1):
        # Check if the handle is present in the 'Codeforces username' column
        if (df.at[i+1,'Codeforces username'] == handle):
    
            if (df.at[i+1,'Round 1'] == ('P') or 
            df.at[i+1,'Round 2'] == ('P') or
            df.at[i+1,'Round 3'] == ('P')):
                # Person is present, append to the updated list
                user['rank'] = j
                j = j+1
                updated_users.append(user)
            print("Added", handle)
            

# Update the 'users' key in the original data dictionary

data['users'] = updated_users

for idx, obj in enumerate(data['users']):
    if idx == 0:
        continue
    
    if obj['total'] == data['users'][idx-1]['total']:
        print(obj)
        data['users'][idx]['rank'] = data['users'][idx - 1]['rank']

# Save the updated JSON data
updated_json_file = 'final.json'
with open(updated_json_file, 'w') as f:
    json.dump(data, f, indent=2)

print("Process completed. Updated JSON data saved to", updated_json_file)
