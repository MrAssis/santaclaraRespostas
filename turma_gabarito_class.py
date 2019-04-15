from typing import Any
import readXls as rx

class turma_gabarito:
    def __init__(self,nome_turma,alunos,prova,gabarito,nome_xlsx):
        self.nome_turma = nome_turma
        self.alunos = alunos
        self.nome_prova = prova
        self.gabarito = gabarito
        self.nome_xlsx = nome_xlsx

    # Gabarito é uma lista com as respostas dessa prova
    def set_gabarito(self,gabarito):
        self.gabarito = gabarito

    # Nome do arquivo que deverá ser lido
    def set_nomeXlsx(self,nome_xlsx):
        self.nome_xlsx = nome_xlsx

    # Listas dos alunos dessa turma
    def set_alunos(self,alunos):
        self.alunos = alunos

    def set_nome_prova(self,nome_prova):
        self.nome_prova = nome_prova

    def set_nome_turma(self,nome_turma):
        self.nome_turma = nome_turma

    # Gabarito é uma lista com as respostas dessa prova
    def get_gabarito(self):
        return self.gabarito

    # Nome do arquivo que deverá ser lido
    def get_nomeXlsx(self):
        return self.nome_xlsx

    # Listas dos alunos dessa turma
    def get_alunos(self):
        return self.alunos

    def get_nome_prova(self):
        return self.nome_prova

    def set_nome_turma(self):
        return self.nome_turma