from menus import menu_produtos

class Produto:
    def __init__(self, nome, codigo, preco_venda, preco_compra, estoque, fornecedor, categoria, ativo=True):
        self.nome = nome
        self.codigo = codigo
        self.ativo = ativo
        self.preco_venda = preco_venda
        self.preco_compra = preco_compra
        self.estoque = estoque
        self.fornecedor = fornecedor
        self.categoria = categoria

    def ativar(self):
        """Ativa o produto."""
        self.ativo = True

    def desativar(self):
        """Desativa o produto."""
        self.ativo = False

    def retirar_do_estoque(self, quantidade=1):
        """Retira quantidade do estoque. Retorna True se bem-sucedido."""
        if quantidade <= 0:
            return False
        if self.estoque < quantidade:
            return False
        self.estoque -= quantidade
        return True
    
    def adicionar_ao_estoque(self, quantidade):
        """Adiciona quantidade ao estoque."""
        if quantidade > 0:
            self.estoque += quantidade
            return True
        return False
    
    @property
    def margem_lucro(self):
        """Calcula a margem de lucro percentual."""
        if self.preco_compra > 0:
            return ((self.preco_venda - self.preco_compra) / self.preco_compra) * 100
        return 0
    
    def __str__(self):
        status = 'Ativo' if self.ativo else 'Inativo'
        return (
            f"Nome: {self.nome}\n"
            f"Código: {self.codigo}\n"
            f"Categoria: {self.categoria}\n"
            f"Fornecedor: {self.fornecedor}\n"
            f"Preço de Compra: R$ {self.preco_compra:.2f}\n"
            f"Preço de Venda: R$ {self.preco_venda:.2f}\n"
            f"Margem de Lucro: {self.margem_lucro:.1f}%\n"
            f"Estoque: {self.estoque} unidades\n"
            f"Status: {status}"
        )

    
def cadastrar_produto():
    """Cadastra um novo produto."""
    print("=" * 70)
    print("CADASTRAR PRODUTO".center(70))
    print("=" * 70)
    
    try:
        nome = input("\nNome do produto: ").strip()
        if not nome:
            print("\nNome não pode ser vazio!")
            return None
            
        codigo = input("Código: ").strip()
        if not codigo:
            print("\nCódigo não pode ser vazio!")
            return None
        
        preco_venda = float(input("Preço de venda: R$ "))
        if preco_venda < 0:
            print("\nPreço de venda não pode ser negativo!")
            return None
            
        preco_compra = float(input("Preço de compra: R$ "))
        if preco_compra < 0:
            print("\nPreço de compra não pode ser negativo!")
            return None
            
        estoque = int(input("Quantidade em estoque: "))
        if estoque < 0:
            print("\nEstoque não pode ser negativo!")
            return None
            
        fornecedor = input("Fornecedor: ").strip()
        categoria = input("Categoria: ").strip()
        
        produto = Produto(nome, codigo, preco_venda, preco_compra, estoque, fornecedor, categoria)
        
        print(f"\nProduto '{nome}' cadastrado com sucesso!")
        return produto
        
    except ValueError:
        print("\nErro: Digite valores numéricos válidos para preços e estoque!")
        return None
    except KeyboardInterrupt:
        print("\n\nCadastro cancelado pelo usuário.")
        return None


def listar_produtos(produtos_cadastrados):
    """Lista todos os produtos cadastrados."""
    if not produtos_cadastrados:
        print("\nNenhum produto cadastrado.")
        return        

    print("=" * 70)
    print("LISTA DE PRODUTOS".center(70))
    print("=" * 70)
    
    for i, produto in enumerate(produtos_cadastrados, 1):
        print(f"\n[{i}]")
        print(produto)
        print("-" * 70)