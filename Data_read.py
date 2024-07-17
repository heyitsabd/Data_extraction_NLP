from openpyxl import load_workbook
import requests
wb = load_workbook('input.xlsx')
ws = wb.active

id_cells = [cell for row in ws['A2':'A' + str(ws.max_row)] for cell in row]
total_count = 0
with open('positive-words.txt','r',encoding='utf-8')as word_file:
    words_to_count=word_file.read().split()
counter =0
def countWords(words_to_count,words):
    word_counts={}
    for word in words_to_count:
        word_counts[word]=words.count(word)
    return sum(word_counts.values())

for id_cell in id_cells:
    url_id=id_cell.value
    try:
        with open(f'./Extracted_Data/{url_id}.txt','r',encoding='utf-8') as file:
            file_Data = file.read()
            words = file_Data.split()
            words_counts=countWords(words_to_count,words)
            total_count += words_counts
    except requests.exceptions.RequestException as e:
        print(f"Error {e}")
                
print(total_count)

