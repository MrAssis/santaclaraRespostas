import readXls as rx

r_1_ano = rx.readSheets_2('gabarito.xlsx',0)
gab = rx.readSheets_2('1_ano_medio.xls',1)

def calculaNota(respostas,gabarito):
    alunos = []
    i = 0
    acerto = 0
    erro = 0
    for r in respostas:
        if i == 0:
            j = 0
            nome = r
            i = 1
        else:
            if r == gabarito[j]:
              acerto = acerto + 1
            else:
                erro = erro + 1
            j = j + 1
            nota = (acerto/66)*100
            a = (nome,acerto,erro,nota)
            alunos.append(a)
    return dict(alunos)

def corrige_certo(res,gabarito_alunos,turma):
    alunos = []
    for gab in gabarito_alunos:
        acerto = 0
        erro = 0
        for j in range(0,len(gab)):
            if j == 0:
                nome = gab[j]
            else:
                if res[turma][j] == gab[j]:
                    acerto = acerto + 1
                else:
                    erro = erro + 1
        perc = (acerto/66)*100
        nota = (acerto/66)*10
        a = (nome,[acerto,erro,perc,nota])
        alunos.append(a)
    return  dict(alunos)

a = corrige_certo(r_1_ano,gab,1)
print(a)