#coding: utf-8

from senador import *
from vetor import *

'''
Tarefa 02 - Comparar o alinhamento de dois senadores
A função abaixo recebe o nome de dois senadores e o
dicionário mapeando o nome do senador com seu objeto
da classe Senador, e retornar o produto interno representando
o grau de similaridade entre a política de voto dos dois senadores dados.
'''
def comparar(sen_a, sen_b, senadores):
	raise NotImplementedError

'''
Tarefa 03 - Encontrar o senador mais similar com um senador dado
A função deve receber o nome de um senador e o dicionário mapeando
o nome do senador com seu objeto da classe Senador, e o nome do senador 
mais similar ao que foi dado como entrada. No caso, de haver mais de um
senador com o grau de similaridade máxima, todos os nomes devem ser retornados
em uma lista.
'''
def mais_similar(sen, senadores):
	raise NotImplementedError

'''
Tarefa 04 - Encontrar o senador menos similar com um senador dado
Similar a tarefa 03, porém deve retornar o nome do senador menos similar
ou uma lista com todos os nomes, em caso de empate.
'''
def menos_similar(sen, senadores):
	raise NotImplementedError

'''
Tarefa 05 - Implementar a função encontra_similaridade_media(sen, sen_set, senadores)
que, dado o nome de um senador, compara seu registro de votos com o registro de votos
com todos os senadores cujos nomes estão em sen_set, computando um produto interno para
cada, e então retornando o produto interno médio.
'''
def encontra_similaridade_media(sen, sen_set, senadores):
	raise NotImplementedError

'''
Tarefa 06 - Implemente a função encontra_registro_medio(sen set, voting dict) que,
dado um conjunto com o nome dos senadores, encontre a média do registro de votação.
Isto é, realize adição vetorial na listas representando o registro de suas votações,
e então divida a soma pelo número de vetores. O resultado deve ser um vetor.
'''
def encontra_registro_medio(sen_set, senadores):
	raise NotImplementedError

'''
Tarefa 07 - Implemente as funções a seguir
- registro_medio_partido(partido, senadores) que, dado o nome de um partido 
  encontra o registro médio de votação deste partido;
- registro_medio_estado(estado, senadores) que, dado o nome de um estado do
  Brasil encontra o registro médio de votação deste estado;
- registro_medio_regiao(regiao, senadores) que, dada o nome de uma região do
  Brasil encontra o registro médio de votação desta região.

O retorno de todas as funções descritas nesta tarefa deve ser um vetor.
'''

def registro_medio_partido(partido, senadores):
	raise NotImplementedError
    
def registro_medio_estado(estado, senadores):
	raise NotImplementedError
    
def registro_medio_regiao(regiao, senadores):
	raise NotImplementedError

'''
Tarefa 08 - Implemente as funções a seguir:
- similaridade_no_partido(sen, senadores) que,
  dado o nome de um senador encontra o grau de similaridade dele com seu partido.
- similaridade_no_estado(sen, senadores) que,
  dado o nome de um senador encontra o grau de similaridade dele com seu estado.
- similaridade_na_regiao(sen, senadores) que,
  dado o nome de um senador encontra o grau de similaridade dele com sua regiao.
  
Para as funções acima o retorno deve ser uma lista contendo o nome do senador e seu respectivo
grau de similaridade.

- encontra_mais_alinhado_partido(partido, senadores) que,
  dado o nome de um partido encontra o senador mais similar ao partido.
  
Para esta última o retorno deve ser o nome do senador.
'''

def similaridade_no_partido(sen, senadores):
	raise NotImplementedError

def similaridade_no_estado(sen, senadores):
	raise NotImplementedError

def similaridade_na_regiao(sen, senadores):
	raise NotImplementedError

def encontra_mais_alinhado_partido(partido, senadores):
	raise NotImplementedError

'''
Tarefa 09 - Implemente as funções a seguir:
- rivais_amargos(senadores) que encontra os dois senadores menos similares do conjunto inteiro.
- amigos_adocicados(senadores) que encontra os dois senadores mais similares do conjunto inteiro.

O retorno deve ser uma lista contendo os nomes dos dois senadores.
'''

def rivais_amargos(senadores):
	raise NotImplementedError

def amigos_adocicados(senadores):
	raise NotImplementedError

'''
Tarefa 10 - Implemente as funções a seguir:
- encontra_partido_mais_coerente(senadores) que encontra o partido
  cujos congressistas são mais similares entre si, ou seja, cuja média das
  similaridades entre cada senador é a maior.
- encontra_partido_menos_coerente(senadores) que encontra o partido
  cujos congressistas são menos similares entre si, ou seja, cuja média das
  similaridades entre cada senador é a menor.
  
O retorno, para ambas, deve ser o nome do partido.
'''

def encontra_partido_mais_coerente(senadores):
	raise NotImplementedError
    
def encontra_partido_menos_coerente(senadores):
	raise NotImplementedError
