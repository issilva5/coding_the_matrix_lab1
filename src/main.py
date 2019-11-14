#coding: utf-8

from deputado import *
from vetor import *

matriculas = ["", "", ""] #Preencham suas matrículas dentro desta variável

'''
Tarefa 02 - Comparar o alinhamento de dois deputados
A função abaixo recebe o nome de dois deputados e o
dicionário mapeando o nome do deputado com seu objeto
da classe Deputado, e retorna o produto interno representando
o grau de similaridade entre a política de voto dos dois deputados dados.
'''
def comparar(dep_a, dep_b, deputados):
	raise NotImplementedError

'''
Tarefa 03 - Encontrar o deputado mais similar com um deputado dado
A função deve receber o nome de um deputado e o dicionário mapeando
o nome do deputado com seu objeto da classe Deputado, e o nome do deputado 
mais similar ao que foi dado como entrada. No caso, de haver mais de um
deputado com o grau de similaridade máxima, todos os nomes devem ser retornados
em uma lista.
'''
def mais_similar(dep, deputados):
	raise NotImplementedError

'''
Tarefa 04 - Encontrar o deputado menos similar com um deputado dado
Similar a tarefa 03, porém deve retornar o nome do deputado menos similar
ou uma lista com todos os nomes, em caso de empate.
'''
def menos_similar(dep, deputados):
	raise NotImplementedError

'''
Tarefa 05 - Implementar a função encontra_similaridade_media(dep, dep_set, deputados)
que, dado o nome de um deputado, compara seu registro de votos com o registro de votos
com todos os deputados cujos nomes estão em dep_set, computando um produto interno para
cada, e então retornando o produto interno médio.
'''
def encontra_similaridade_media(dep, dep_set, deputados):
	raise NotImplementedError

'''
Tarefa 06 - Implemente a função encontra_registro_medio(dep_set, voting_dict) que,
dado um conjunto com o nome dos deputados, encontre a média do registro de votação.
Isto é, realize adição vetorial na listas representando o registro de suas votações,
e então divida a soma pelo número de vetores. O resultado deve ser um vetor.
'''
def encontra_registro_medio(dep_set, deputados):
	raise NotImplementedError

'''
Tarefa 07 - Implemente as funções a seguir
- registro_medio_partido(partido, deputados) que, dado o nome de um partido 
  encontra o registro médio de votação deste partido;
- registro_medio_estado(estado, deputados) que, dado o nome de um estado do
  Brasil encontra o registro médio de votação deste estado;
- registro_medio_regiao(regiao, deputados) que, dada o nome de uma região do
  Brasil encontra o registro médio de votação desta região.

O retorno de todas as funções descritas nesta tarefa deve ser um vetor.
'''

def registro_medio_partido(partido, deputados):
	raise NotImplementedError
    
def registro_medio_estado(estado, deputados):
	raise NotImplementedError
    
def registro_medio_regiao(regiao, deputados):
	raise NotImplementedError

'''
Tarefa 08 - Implemente as funções a seguir:
- similaridade_no_partido(dep, deputados) que,
  dado o nome de um deputado encontra o grau de similaridade dele com seu partido.
- similaridade_no_estado(dep, deputados) que,
  dado o nome de um deputado encontra o grau de similaridade dele com seu estado.
- similaridade_na_regiao(dep, deputados) que,
  dado o nome de um deputado encontra o grau de similaridade dele com sua regiao.
- encontra_mais_alinhado_partido(partido, deputados) que,
  dado o nome de um partido encontra o deputado mais similar ao partido.
  
Para as funções acima o retorno deve ser uma lista contendo o nome do deputado e seu respectivo
grau de similaridade.
'''

def similaridade_no_partido(dep, deputados):
	raise NotImplementedError

def similaridade_no_estado(dep, deputados):
	raise NotImplementedError

def similaridade_na_regiao(dep, deputados):
	raise NotImplementedError

def encontra_mais_alinhado_partido(partido, deputados):
	raise NotImplementedError

'''
Tarefa 09 - Implemente as funções a seguir:
- rivais_amargos(deputados) que encontra os dois deputados menos similares do conjunto inteiro.
- amigos_adocicados(deputados) que encontra os dois deputados mais similares do conjunto inteiro.

O retorno deve ser uma lista contendo os nomes dos dois deputados.
'''

def rivais_amargos(deputados):
	raise NotImplementedError

def amigos_adocicados(deputados):
	raise NotImplementedError

'''
Tarefa 10 - Implemente as funções a seguir:
- encontra_partido_mais_coerente(deputados) que encontra o partido
  cujos congressistas são mais similares entre si, ou seja, cuja média das
  similaridades entre cada deputado é a maior.
- encontra_partido_menos_coerente(deputados) que encontra o partido
  cujos congressistas são menos similares entre si, ou seja, cuja média das
  similaridades entre cada deputado é a menor.
  
O retorno, para ambas, deve ser o nome do partido.
'''

def encontra_partido_mais_coerente(deputados):
	raise NotImplementedError
    
def encontra_partido_menos_coerente(deputados):
	raise NotImplementedError
