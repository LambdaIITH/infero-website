import pandas as pd
import json
import requests
from bs4 import BeautifulSoup
# Load Excel data into a DataFrame
excel_file = 'data.xlsx'
df = pd.read_excel(excel_file)

users = []
for i in range(len(df)-1):
    user = df.at[i,'Codeforces username']
    # print(user)
    info = requests.get(f'https://codeforces.com/profile/{user}')
    soup = BeautifulSoup(info.text, 'html.parser')
    if soup.find('div',class_ = 'main-info') is not None:
        name = soup.find('div',class_ = 'main-info').find('h1').text.removeprefix('\n').strip(' ')
        print(name)
        df.at[i,'Codeforces username'] = name
    
df.to_excel('updated_data.xlsx',index=False)