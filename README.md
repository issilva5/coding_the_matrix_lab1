# Laboratório: Como vota o nosso congresso?

Neste laboratório, iremos estudar o padrão de votação dos nossos parlamentares. Queremos saber qual parecido são os votos, em particular, se as bancadas de cada partido votam de maneira coerente. O registro de voto de cada deputado será representado por um vetor cujas entradas podem ser 0, 1 ou -1, indicando que o parlamentar votou por abstenção, sim ou não numa data proposta, respectivamente.

## A estrutura de laboratório

Este repositório está organizado em três partes principais: um [Jupyter Notebook](descricao.ipynb) descrevendo como a implementação deve ser feita; um [diretório](src) contendo o código de análise (usaremos Python 3); e um outro diretório contendo o [conjunto de dados a ser analisado](src).

### Jupyter Notebook

Este [notebook](descricao.ipynb) descreve quais funcionalidades devem ser implementadas neste laboratório. Além disso, fornece exemplos de como utilizar o código base disponibilizado.

### Análise

O diretório [src](src) contém uma base de código que precisará ser modificada para implementar as funcionalidades requisitadas. Esta base de código inclue:
 - ```vetor.py```, no qual devem ser implementadas as operações sobre vetores, tais como: soma, produto por escalar, produto interno, entre outras;
 - ```deputado.py```, implementa a classe Deputado que será utilizada no laboratório para encapsular e abstrair a representação do parlamentar.
 - ```file_reader.py```, disponibiliza a função ```ler_votacao```, a qual realiza a leitura dos dados de votação e retorna um dicionário que tem como chave o nome do parlamentar, e como item um objeto da classe Deputado.
 - ```main.py```, classe principal do laboratório, nela devem ser implementadas as rotinas deste laboratório.
 - ```my_tests.py```, classe disponível contendo casos de testes para a verificação da implementação do laboratório.

### Conjunto de dados

Nosso [conjunto de dados](data) contém dois arquivos. O arquivo ```exemplo.csv```, contém um pequeno trecho do conjunto completo de dados disponível no segundo arquivo, ```votos.csv```.

## Agradecimentos

[Itallo Silva](https://github.com/issilva5) por ter criado a descrição e o código base deste projeto.
[Jefferson Neves](https://github.com/jeffersonrpn) por ter disponibilizado a base de dados.

