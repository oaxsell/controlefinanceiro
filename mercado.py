from menus import menu_mercados

class Mercado:
    def __init__(self, nome, midia, ativo):
        self.nome = nome
        self.midia = midia
        self.ativo = ativo

    def ativar(self):
        self.ativo = True

    def desativar(self):
        self.ativo = False
    
    def __str__(self):
        status = 'ativo' if self.ativo else 'inativo'
        return f"Nome: {self.nome}, Site: {self.midia}, Status: {status}"

def pausar():
    input("\nPressione ENTER para continuar...")
    print("\033[2J\033[H", end="")

def cadastrar_mercado():
    print("CADASTRAR MERCADO")    
    nome = input("Nome do mercado: ")
    site = input("Site: ")
    mercado = Mercado(nome, site, True)
    print(f"\nMercado '{nome}' cadastrado com sucesso!")
    pausar()
    return mercado

def listar_mercados(mercados_cadastrados):
    if not mercados_cadastrados:
        print("\nNenhum mercado cadastrado.")
        return        

    print("LISTA DE MERCADOS")
    for mercado in mercados_cadastrados:
        print(mercado)
        print("-"*70)
    pausar()