import pandas as pd
import json
import sys

# Load Excel data into a DataFrame
excel_file = 'updated_data.xlsx'
df = pd.read_excel(excel_file)

num_contests = int(sys.argv[1])

# Load JSON data
json_file = 'final.json'
with open(json_file, 'r') as f:
    data = json.load(f)

users_list = data['users']

# to check if the user has participated in the contest

for userData in users_list:
    handle = userData['handle']
    cur_bool = False
    for cur_cont in range(1, num_contests+1): # iterate over all contests
        for idx, row in df.iterrows(): # iterate over all rows in the Excel file
            if row['Codeforces username'] == handle:
                if row[f'Round {cur_cont}'] != 'P':
                    cur_bool = True
                    userData[f'contest_{cur_cont}'] = 0
                    break
    if not cur_bool: # if the user has participated in no contest, remove the user
        users_list.remove(userData)
        print("Removed", handle)
    
    arr = sorted([userData[f'contest_{i}'] for i in range(1, num_contests+1)], reverse= True)[:3]
    
    userData['total'] = sum(arr)

users_list.sort(key=lambda x: x['total'], reverse=True)

# creating the ranks in a new list
for idx,userData in enumerate(users_list):
    userData['rank'] = idx + 1
            

# Update the 'users' key in the original data dictionary

data['users'] = users_list

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
