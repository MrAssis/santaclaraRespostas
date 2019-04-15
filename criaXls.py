import xlrd as ex
import xlwt as ew
name = 'turmas.xlsx'
wb = ex.open_workbook(name)
ano_3 = wb.sheet_by_index(0).col_values(0)
ano_2 = wb.sheet_by_index(1).col_values(0)
ano_1 = wb.sheet_by_index(2).col_values(0)
print(ano_1)

wb_2 = ew.Workbook()
ws = wb_2.add_sheet('teste')
ws.write(0,0,u'teste1')
wb_2.save('first.xls')

def cria(alunos, nome_arquivo):
    workB = ew.Workbook()
    j = 1
    for a in alunos:
        ws = workB.add_sheet(str(j))
        ws.write(0,0,'Questão')
        ws.write(0,1,a)
        for i in range(1,67):
            ws.write(i,0 ,i)
        j = j + 1
    workB.save(nome_arquivo)


cria(ano_1,'1_ano_medio.xls')
cria(ano_2,'2_ano_medio.xls')
cria(ano_3,'3_ano_medio.xls')