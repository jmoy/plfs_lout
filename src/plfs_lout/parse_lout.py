import openpyxl
import re

def parse(filename:str):
    wb = openpyxl.load_workbook(filename,read_only=True)
    sheet = wb.worksheets[0]
    rows =[[v for v in r] for r in sheet.values]
    files = _parse_files(rows)
    return files

def _parse_files(rows):
    res = []
    while True:
        f,rows = _parse_file(rows)
        if f is None:
            break
        else:
            res.append(f)
    return res

def _parse_file(rows):
    for i in range(len(rows)):
        match = re.search(r'File:\s*(.+)\.txt',
                            str(rows[i][0]),
                            re.IGNORECASE)
        if match:
            fname = match.group(1).lower()
            coldescs,rows = _parse_cols(rows[i+2:])
            return (fname,coldescs),rows
    return None,[]

def _parse_cols(rows):
    cols = []
    for i in range(len(rows)):
        if not re.search(r'\s*\d+',str(rows[i][0])):
            break
        col_name = _normalize_name(rows[i][1])
        col_width = rows[i][4]
        cols.append((col_name,col_width))
    return cols,rows[i:]

noise_words = {'for','of','in','on'}
def _normalize_name(name):
    compos = re.split(r'\W+',name)
    compos = [s.lower() for s in compos]
    compos = [s for s in compos 
                if s and s not in noise_words]
    return '_'.join(compos)