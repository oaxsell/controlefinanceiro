from menus import menu_mercados, menu_principal, menu_produtos
from mercado import Mercado, cadastrar_mercado, listar_mercados
from produto import Produto, cadastrar_produto, listar_produtos
from exportacao import salvar_mercados_csv

def main():
    # Inicializar listas de mercados e produtos
    mercados_cadastrados = []
    produtos_cadastrados = []
    menu_principal()
    opcao = input("\nEscolha uma opção: ")
    while True:
        match opcao:
            case "1":
                while True:
                    menu_produtos()
                    opcao = input("\nEscolha uma opção: ")
                    match opcao:
                        case "1":
                            novo_produto = cadastrar_produto() 
                            if novo_produto:
                                produtos_cadastrados.append(novo_produto)
                        case "2":
                            listar_produtos(produtos_cadastrados)
                        case "3":
                            codigo_produto = input("Digite o código do produto para ativar/desativar: ")
                            for produto in produtos_cadastrados:
                                if produto.codigo == codigo_produto:
                                    if produto.ativo:
                                        produto.desativar()
                                        print(f"Produto '{produto.nome}' desativado com sucesso!")
                                    else:
                                        produto.ativar()
                                        print(f"Produto '{produto.nome}' ativado com sucesso!")
                                    break
                        case "0":
                            break
                        case _:
                            print("\n✗ Opção inválida!")
                            break
            case "2":
                menu_mercados()
                opcao = input("\nEscolha uma opção: ")
                match opcao:
                    case "1":
                        novo_mercado = cadastrar_mercado() 
                        if novo_mercado:
                            mercados_cadastrados.append(novo_mercado)
                    case "2":
                        listar_mercados(mercados_cadastrados)
                    case "3":
                        nome_mercado = input("Digite o nome do mercado para ativar/desativar: ")
                        for mercado in mercados_cadastrados:
                            if mercado.nome == nome_mercado:
                                if mercado.ativo:
                                    mercado.desativar()
                                    print(f"Mercado '{mercado.nome}' desativado com sucesso!")
                                else:
                                    mercado.ativar()
                                    print(f"Mercado '{mercado.nome}' ativado com sucesso!")
                                break
                    case "0":
                        break
                    case _:
                        print("\n✗ Opção inválida!")
            case "3":
                print("\nEXPORTAR MERCADOS PARA CSV")
                print("1 - Exportar mercados cadastrados para CSV")
                print("2 - Exportar produtos cadastrados para CSV")
                opcao_exportacao = input("\nEscolha uma opção: ")
                match opcao_exportacao:
                    case "1":
                        nome_arquivo = input("Digite o nome do arquivo CSV para salvar os mercados: ")
                        salvar_mercados_csv(mercados_cadastrados, nome_arquivo)
                    case "2":
                        nome_arquivo = input("Digite o nome do arquivo CSV para salvar os produtos: ")
                        salvar_mercados_csv(produtos_cadastrados, nome_arquivo)
                    case _:
                        print("\n✗ Opção inválida!")
            case "0":
                print("\nSaindo do sistema...")
                break
            case _:
                print("\n✗ Opção inválida!")
                break

if __name__ == "__main__":
    main()