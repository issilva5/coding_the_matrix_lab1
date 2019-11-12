#coding: utf-8

class Vetor:
    
    '''
    Inicializa o vetor a partir de uma lista.
    @param lista Lista contendo os elementos que devem ser as entradas do vetor.
    '''
    def __init__(self, lista):
        self.entradas = lista
        self.size = len(lista)
    
    '''
    Retorna a dimensão do vetor.
    '''
    def __len__(self):
        return self.size
    
    '''
    Retorna o item numa dada posição.
    '''
    def __getitem__(self, index):
        return self.entradas[index]
    
    '''
    Implementa a operação de soma entre vetores.
    Você pode assumir que ambos os vetores têm a mesma dimensão.
    @param vetor Vetor que deve ser adicionado
    @return objeto da classe Vetor representando o vetor resultante.
    '''
    def __add__(self, vetor):
        raise NotImplementedError
    
    def __radd__(self, vetor):
        return self.__add__(vetor)
    
    '''
    Implementa a operação de multiplicação por escalar ou produto interno.
    Você pode assumir que ambos os vetores têm a mesma dimensão.
    @param mult pode ser um escalar ou pode ser outro Vetor
    @return objeto da classe Vetor representando o vetor resultante, caso
            mult seja escalar, ou um escalar representado o produto interno
            caso mult seja outro vetor.
    '''
    def __mul__(self, mult):
        
        '''
        Implementa a multiplicação por escalar
        '''
        if isinstance(mult, float) or isinstance(mult, int):
            raise NotImplementedError
        
        '''
        Implementa o produto vetorial
        '''
        if isinstance(mult, Vetor):
            raise NotImplementedError
    
    def __rmul__(self, mult):
        return self.__mul__(mult)
    
    def __sub__(self, vetor):
        return self.__add__(vetor * -1)
    
    def __rsub__(self, vetor):
        return vetor.__sub__(self)
    
    '''
    Implementa a divisão por escalar.
    '''
    def __truediv__(self, fator):
        return self.__mul__(1.0/fator);
    
    '''
    Implementa a igualdade entre vetores
    @param vetor Vetor a ser comparado
    @return boolean True se forem igual, False caso contrário
    '''
    def __eq__(self, vetor):
        raise NotImplementedError
    
    def __neq__(self, vetor):
        return not self.__eq__(vetor)
    
    '''
    Implementa uma representação textual para o vetor.
    '''
    def __str__(self):
        return "Vetor" + str(self.entradas)
