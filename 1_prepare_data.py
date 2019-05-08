# encoding: utf-8

import xlrd

raw_data_path = r"raw_data/nlu语料全部(2).xlsx"

workbook = xlrd.open_workbook(raw_data_path)

data = workbook.sheet_by_index(0)

rows = data.nrows

result = dict()

for row in range(1,rows):
    slot = data.cell(row,0).value.strip()
    if len(slot) == 0:
        continue
    sentence = data.cell(row,1).value.strip()
    if len(sentence) == 0:
        continue

    if slot not in result:
        result[slot] = [sentence.replace("\n","")]
    else:
        result[slot].append(sentence.replace("\n",""))

# generating pairs
outfile_path = r'data/corpus.pairs.txt'
outfile = open(outfile_path,'w',encoding="utf-8")
for slot,sentences in result.items():
    for s1 in sentences:
        for s2 in sentences:
            if s1 != s2:
                outfile.write("{s1}#^#{s2}#^#{slot}\n".format(s1=s1,s2=s2,slot=slot))

outfile.close()
