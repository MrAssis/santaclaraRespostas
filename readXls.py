import xlrd as ex

def readSheets(name):
    wb = ex.open_workbook(name)
    alunos = []
    for i in range(0,len(wb.sheets())):
        s = wb.sheet_by_index(i)
        a = readSheet(s)
        a.append(s.name)
        alunos.append(a)
    return alunos

def readSheet(s):
    alt = []
    for j in range(1,67):
        alt.append(s.row_values(j))
    return alt

def readSheets_2(name,col):
    wb = ex.open_workbook(name)
    alunos = []
    for i in range(0, len(wb.sheets())):
        s = wb.sheet_by_index(i)
        a = s.col_values(col)
        alunos.append(a)
    return alunos

