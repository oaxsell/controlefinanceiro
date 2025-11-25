def salvar_mercados_csv(dados_a_exportar, nome_arquivo):
    import csv
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(['Nome', 'Site', 'Ativo'])
        for dados in dados_a_exportar:
            escritor.writerow([dados])
    print(f"\nMercados salvos em '{nome_arquivo}' com sucesso!")