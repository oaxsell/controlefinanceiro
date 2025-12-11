from menus import menu_mercados, menu_principal, menu_produtos
from mercado import Mercado, cadastrar_mercado, listar_mercados
from produto import Produto, cadastrar_produto, listar_produtos
from exportacao import salvar_mercados_csv


class SistemaGerenciamento:
    """Sistema de gerenciamento de mercados e produtos."""
    
    def __init__(self):
        self.mercados = []
        self.produtos = []
    
    @staticmethod
    def limpar_tela():
        """Limpa a tela do console."""
        print("\033[2J\033[H", end="")
    
    def toggle_status_produto(self):
        """Ativa ou desativa um produto."""
        codigo = input("Digite o código do produto para ativar/desativar: ")
        self.limpar_tela()
        
        produto = next((p for p in self.produtos if p.codigo == codigo), None)
        
        if produto:
            if produto.ativo:
                produto.desativar()
                print(f"✓ Produto '{produto.nome}' desativado com sucesso!")
            else:
                produto.ativar()
                print(f"✓ Produto '{produto.nome}' ativado com sucesso!")
        else:
            print(f"✗ Produto com código '{codigo}' não encontrado!")
    
    def toggle_status_mercado(self):
        """Ativa ou desativa um mercado."""
        nome = input("Digite o nome do mercado para ativar/desativar: ")
        
        mercado = next((m for m in self.mercados if m.nome == nome), None)
        
        if mercado:
            if mercado.ativo:
                mercado.desativar()
                print(f"✓ Mercado '{mercado.nome}' desativado com sucesso!")
            else:
                mercado.ativar()
                print(f"✓ Mercado '{mercado.nome}' ativado com sucesso!")
        else:
            print(f"✗ Mercado '{nome}' não encontrado!")
        
        self.limpar_tela()
    
    def menu_produtos(self):
        """Gerencia o submenu de produtos."""
        acoes = {
            "1": self._cadastrar_produto,
            "2": self._listar_produtos,
            "3": self.toggle_status_produto,
        }
        
        while True:
            menu_produtos()
            opcao = input("\nEscolha uma opção: ")
            self.limpar_tela()
            
            if opcao == "0":
                print("Voltando ao menu principal...")
                break
            
            acao = acoes.get(opcao)
            if acao:
                acao()
            else:
                print("✗ Opção inválida!")
    
    def _cadastrar_produto(self):
        """Cadastra um novo produto."""
        novo_produto = cadastrar_produto()
        self.limpar_tela()
        if novo_produto:
            self.produtos.append(novo_produto)
    
    def _listar_produtos(self):
        """Lista todos os produtos cadastrados."""
        listar_produtos(self.produtos)
        self.limpar_tela()
    
    def menu_mercados(self):
        """Gerencia o submenu de mercados."""
        acoes = {
            "1": self._cadastrar_mercado,
            "2": self._listar_mercados,
            "3": self.toggle_status_mercado,
        }
        
        while True:
            menu_mercados()
            opcao = input("\nEscolha uma opção: ")
            self.limpar_tela()
            
            if opcao == "0":
                print("Voltando ao menu principal...")
                break
            
            acao = acoes.get(opcao)
            if acao:
                acao()
            else:
                print("✗ Opção inválida!")
    
    def _cadastrar_mercado(self):
        """Cadastra um novo mercado."""
        novo_mercado = cadastrar_mercado()
        if novo_mercado:
            self.mercados.append(novo_mercado)
    
    def _listar_mercados(self):
        """Lista todos os mercados cadastrados."""
        listar_mercados(self.mercados)
    
    def menu_exportacao(self):
        """Gerencia o menu de exportação."""
        print("\nEXPORTAR PARA CSV")
        print("1 - Exportar mercados cadastrados")
        print("2 - Exportar produtos cadastrados")
        print("0 - Voltar")
        
        opcao = input("\nEscolha uma opção: ")
        self.limpar_tela()
        
        if opcao == "1":
            self._exportar_dados(self.mercados, "mercados")
        elif opcao == "2":
            self._exportar_dados(self.produtos, "produtos")
        elif opcao == "0":
            print("Voltando ao menu principal...")
        else:
            print("✗ Opção inválida!")
    
    def _exportar_dados(self, dados, tipo):
        """Exporta dados para CSV."""
        nome_arquivo = input(f"Digite o nome do arquivo CSV para salvar os {tipo}: ")
        salvar_mercados_csv(dados, nome_arquivo)
    
    def executar(self):
        """Loop principal do sistema."""
        acoes_principal = {
            "1": self.menu_produtos,
            "2": self.menu_mercados,
            "3": self.menu_exportacao,
        }
        
        while True:
            menu_principal()
            opcao = input("\nEscolha uma opção: ")
            self.limpar_tela()
            
            if opcao == "0":
                print("\nSaindo do sistema...")
                break
            
            acao = acoes_principal.get(opcao)
            if acao:
                acao()
            else:
                print("✗ Opção inválida!")


def main():
    """Função principal do programa."""
    sistema = SistemaGerenciamento()
    sistema.executar()


if __name__ == "__main__":
    main()
