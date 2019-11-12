#coding: utf-8

import csv
from senador import *
from vetor import *

'''
Leitura e manipulação do arquivo
'''

def ler_votacao(path):

	f = open(path, 'r')
	csv_file = csv.reader(f)
	headers = next(csv_file, None)

	voting_dict = {}

	for row in csv_file:
		sen_nome = row[0]
		sen_estado = row[1]
		sen_partido = row[2]
		sen_votos = list(map(int, row[3:len(row)]))
		voting_dict[sen_nome] = Senador(sen_nome, sen_estado, sen_partido, Vetor(sen_votos))

	return voting_dict
