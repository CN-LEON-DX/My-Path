import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'

table_name = 'Top_50'
csv_path =  '/home/project/top_50_films.csv'

df = pd.DataFrame(columns=['Average Rank', 'Film', 'Year'])

count = 0

# get data
html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')

tables = data.find_all('tbody')
rows = tables[0].find_all('tr')

# print(tables)
# print(rows)
for row in rows:
    if count < 50:
        col = row.find_all('td')
        if len(col) != 0:
            data_dict = {
                "Average Rank" : col[0].text,
                "Film": col[1].text,
                "Year": col[2].text
            }
            # print(data_dict)
            # create new df has only 1 row
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)
            count+=1
            # print(df1)
            # print(df)
    else:
        break

print(df.head(1))
# result
#   Average Rank           Film  Year
# 0            1  The Godfather  1972

df.to_csv(csv_path)

# save it to database 
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()