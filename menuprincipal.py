from mercado import Mercado
# Se eu progranmo sem OO, eu sou um programador procedural
# Funcoes soltas, estruturas sequenciais e dicionarios.



# Criar um dicionario mercado nome, site ativo
mercado = {
    "nome": "Tudo bem",
    "midia": "www.mercadolivre.com.br",
    "ativo": False
}


m1 = Mercado("Tudo bem", "www.tudobom.com.br", False)
m2 = Mercado("Compra Facil", "www.comprafacil.com.br", True)
m3 = Mercado("Mercado Legal", "www.mercadolegal.com.br", False)
m4 = Mercado("Supermercado Show", "www.supermercadoshow.com.br", True)

print(m1.ativo)
m1.ativar()
print(m1.ativo)
m1.desativar()
print(m1.ativo)

mercados = [m1, m2, m3, m4]


    
print(vars(m1))
print(dir(m1))
print(m1)