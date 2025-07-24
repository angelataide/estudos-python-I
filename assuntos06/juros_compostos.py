# %%

def juros_compostos(aporte,taxa, anos):
    """ juros_compose serve para calcular o retorno financeiro a partir de um aporte. Deve-se considerar o valor, a taxa de juros atual e o tempo (em anos) para cálculo do valor a ser retornado. 
    
    aporte:
        um número inteiro, que represente o valor em R$
    
    taxa:
        um número float entre 0 e 1 que represente o valor taxa de juros
        
    anos:
        um número inteiro >= 1 que representa o tempo que o investimento terá liquidez
    """
    
    return aporte * (1 + taxa) ** anos

# %%

juros_compostos(aporte =1000, taxa =0.13, anos =4)

# %%
