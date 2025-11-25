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

def cadastrar_mercado():
    print("CADASTRAR MERCADO")    
    nome = input("Nome do mercado: ")
    site = input("Site: ")
    mercado = Mercado(nome, site, True)
    print(f"\nMercado '{nome}' cadastrado com sucesso!")
    return mercado

def listar_mercados(mercados_cadastrados):
    if not mercados_cadastrados:
        print("\nNenhum mercado cadastrado.")
        return        

    print("LISTA DE MERCADOS")
    for mercado in mercados_cadastrados:
        print(mercado)
        print("-"*70)

def gerenciar_mercados():
    while True:
        menu_mercados()
        opcao = input("\nEscolha uma opção: ")
        
        match opcao:
            case "1":
                cadastrar_mercado()
                pausar()
            case "2":
                Mercado.listar_mercados()
                pausar()
            case "3":
                print("\n(Funcionalidade de ativar/desativar mercado)")
                pausar()
            case "0":
                break
            case _:
                print("\n✗ Opção inválida!")
                pausar()