from openpyxl import load_workbook

# Load the workbooks and select the active worksheets
input_wb = load_workbook('input.xlsx')
input_ws = input_wb.active

output_wb = load_workbook('Output Data Structure.xlsx')
output_ws = output_wb.active


id_cells = [cell for row in input_ws['A2':'A' + str(input_ws.max_row)] for cell in row]
result_positive_cell_id = [cell for row in output_ws['C2':'C' + str(output_ws.max_row)] for cell in row]

with open('positive-words.txt', 'r', encoding='utf-8') as word_file:
    words_to_count = word_file.read().split()

def countWords(words_to_count, words):
    total_words = 0
    for word in words_to_count:
        total_words += words.count(word)
    return total_words

results = {}
for id_cell in id_cells:
    url_id = id_cell.value
    try:
        with open(f'./Extracted_Data/{url_id}.txt', 'r', encoding='utf-8') as file:
            file_data = file.read()
            words = file_data.split() 
            words_counts = countWords(words_to_count, words)
            results[url_id] = words_counts
    except Exception as e:
        print(f"Error for {url_id}: {e}")

# Write the results to the output Excel file
for idx, id_cell in enumerate(id_cells):
    url_id = id_cell.value
    if url_id in results:
        result_positive_cell_id[idx].value = results[url_id]

# Save the updated output Excel file
output_wb.save('Output Data Structure.xlsx')

print("Word counts have been successfully written to the output Excel file.")
