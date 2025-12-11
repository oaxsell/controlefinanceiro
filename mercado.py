from menus import menu_mercados

class Mercado:
    def __init__(self, nome, midia, ativo=True):
        self.nome = nome
        self.midia = midia
        self.ativo = ativo

    def ativar(self):
        self.ativo = True

    def desativar(self):
        self.ativo = False
    
    def __str__(self):
        status = 'Ativo' if self.ativo else 'Inativo'
        return f"Nome: {self.nome}\nSite: {self.midia}\nStatus: {status}"

def cadastrar_mercado():
    """Cadastra um novo mercado."""
    print("CADASTRAR MERCADO")    
    nome = input("Nome do mercado: ")
    site = input("Site: ")
    
    mercado = Mercado(nome, site)
    print(f"\nMercado '{nome}' cadastrado com sucesso!")
    
    return mercado


def listar_mercados(mercados_cadastrados):
    """Lista todos os mercados cadastrados."""
    if not mercados_cadastrados:
        print("\nNenhum mercado cadastrado.")
        return        

    print("=" * 70)
    print("LISTA DE MERCADOS".center(70))
    print("=" * 70)
    
    for i, mercado in enumerate(mercados_cadastrados, 1):
        print(f"\n[{i}]")
        print(mercado)
        print("-" * 70)
