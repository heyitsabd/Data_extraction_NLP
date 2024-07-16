from openpyxl import load_workbook
import requests
from bs4 import BeautifulSoup
import pandas as pd

wb = load_workbook('input.xlsx')
ws = wb.active

#+ str(ws.max_row)
cell_range = ws['B2':'B'+ str(ws.max_row) ]

data={'URL_ID':[],'WebData':[]}
count =0
for cell in cell_range:
    for x in cell:
        url = x.value
        try:
            response = requests.get(url)
            response.raise_for_status()  
            soup = BeautifulSoup(response.text, 'html.parser')
            count=count+1
            headings1 = soup.select(' h1.wp-block-heading')
            headings3 = soup.select(' h3.wp-block-heading')
            articles = soup.select('div.td-ss-main-content p ')
            for heading in headings1:
                data['WebData'].append(heading.string)
            for heading in headings3:
                data['WebData'].append(heading.string)
            for article in articles:
                data['WebData'].append(article.string)
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")

df= pd.DataFrame.from_dict(data)
df.to_('result.xlsx')