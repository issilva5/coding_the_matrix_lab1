from file_reader import *
from main import *

deputados = ler_votacao("data/votos.csv")

def test(got, expected):
    if isinstance(got, float) and isinstance(expected, float):
        if abs(got - expected) <= 0.0001:
            print("OK! got: " + str(got) + ", expected: " + str(expected))
            return 1
        else:
            print("WA! got: " + str(got) + ", expected: " + str(expected))
            return 0
    else:
        if got == expected:
            print("OK! got: " + str(got) + ", expected: " + str(expected))
            return 1
        else:
            print("WA! got: " + str(got) + ", expected: " + str(expected))
            return 0

#TAREFA 01
a = Vetor([1, 2, 3, 4])
b = Vetor([4, 3, 2, 1])

test(a == b, False)
test(a + b, Vetor([5, 5, 5, 5]))
test(a - b, Vetor([-3, -1, 1, 3]))

#TAREFA 02
test(comparar("141422", "178883", deputados), 207)

#TAREFA 03
test(mais_similar("4930", deputados), "74378")
test(mais_similar("74163", deputados), ['178993', '178871'])

#TAREFA 04
test(menos_similar("200153", deputados), "132504")

#TAREFA 05
test(encontra_similaridade_media("105112", ["178918",  "74378",  "74383", "141445",  "97707", "160544", "199809", "178983", "141440"], deputados), 51.5555)