# Laboratório: Comparando políticas de votação

Neste laboratório, iremos usar vetores para avaliar objetivamente a mentalidade política dos senadores que nós representam. O registro de voto de cada senador será representado por um vetor cujas entradas podem ser 0, 1 ou -1, indicando que o parlamentar votou por abstenção, sim ou não numa dada lei, respectivamente. A partir da diferença entre os "vetores de votação" de dois senadores, nós podemos dissipar a neblina da política e ver como nossos representantes se posicionam, utilizando para isso o produto interno.

## A estrutura de laboratório

Este repositório está dividido em três partes principais: um Jupyter Notebook descrevendo como a implementação deve ser feita; um pasta contendo o código fonte; e uma pasta contendo o arquivo de dados. Como linguagem de programação foi escolhida Python3, devido ao seu alto nível, popularidade e facilidade de implementação.

### Jupyter Notebook

Disponível [aqui](descricao.ipynb), este notebook descreve quais funcionalidades devem ser implementadas neste laboratório, além de fornecer pequenos exemplos de como utilizar as classes disponíveis no projeto.

### A pasta source

A pasta [scr](src) é onde se encontram os arquivos de código que devem ser modificados para a implementação das funcionalidades deste laboratório. São eles:
 - vetor.py, onde devem ser implementadas as operações de um vetor, tais como: soma entre vetores, produto por escalar, produto interno, entre outras.
 - senador.py, implementa a classe Senador que será utilizada no laboratório para encapsular e abstrair a representação do parlamentar.
 - file_reader.py, disponibiliza uma a função ler_votacao, a qual realiza a leitura dos dados de votação e retorna um dicionário que tem como chave o nome do parlamentar, e como item um objeto da classe Senador.
 - main.py, classe principal do laboratório, nela devem ser implementadas as rotinas deste laboratório.
 - my_tests.py, classe disponível contendo casos de testes para a verificação da implementação do laboratório.

### A pasta data

A pasta [data](data) contém os arquivos de dados usados neste laboratório. O arquivo exemplo.csv, contém um pequeno exemplo de como é o arquivo real de dados, e é utilizado no Notebook para descrever como realizar a leitura de um csv em Python. O arquivo votos.csv, contém de fato o arquivo deve ser utilizado como entrada para os testes do laboratório.

## Agradecimentos


