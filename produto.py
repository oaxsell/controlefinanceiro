from menus import menu_produtos

class Produto:
    def __init__(self, nome, codigo, ativo, preco_venda, preco_compra, estoque, fornecedor, categoria):
        self.nome = nome
        self.codigo = codigo
        self.ativo = ativo
        self.preco_venda = preco_venda
        self.preco_compra = preco_compra
        self.estoque = estoque
        self.fornecedor = fornecedor
        self.categoria = categoria

    def ativar(self):
        self.ativo = True

    def desativar(self):
        self.ativo = False

    def retirar_do_estoque(self, quantidade=1):
        if self.estoque < quantidade:
            return False
        self.estoque -= quantidade
        return True
    
    def adicionar_ao_estoque(self, quantidade):
        self.estoque += quantidade
    
    def __str__(self):
        status = 'ativo' if self.ativo else 'inativo'
        return f"Produto: {self.nome} (Código: {self.codigo}) - Status: {status} - Estoque: {self.estoque}"
    
def cadastrar_produto():
    print("CADASTRAR PRODUTO")    
    try:
        nome = input("Nome do produto: ")
        codigo = input("Código: ")
        preco_venda = float(input("Preço de venda: R$ "))
        preco_compra = float(input("Preço de compra: R$ "))
        estoque = int(input("Quantidade em estoque: "))
        fornecedor = input("Fornecedor: ")
        categoria = input("Categoria: ")
        
        produto = Produto(nome, codigo, True, preco_venda, preco_compra, estoque, fornecedor, categoria)
        
        print(f"\n✓ Produto '{nome}' cadastrado com sucesso!")
        return produto
    except Exception as e:
        print(f"\n✗ Erro ao cadastrar produto: {e}")
        return None

def listar_produtos(produtos_cadastrados):
    if not produtos_cadastrados:
        print("\nNenhum mercado cadastrado.")
        return        

    print("LISTA DE MERCADOS")
    for produto in produtos_cadastrados:
        print(produto)
        print("-"*70)
        