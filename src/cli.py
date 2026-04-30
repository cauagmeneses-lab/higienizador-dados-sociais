import argparse
import os
from limpador import processar_csv


def main():
    parser = argparse.ArgumentParser(
        description="Higienizador de Dados - Limpa planilhas bagunçadas."
    )

    parser.add_argument("entrada", help="Caminho para o CSV sujo")

    parser.add_argument(
        "--saida",
        default="dados_limpos.csv",
        help="Nome do arquivo CSV de saída (opcional)"
    )

    args = parser.parse_args()

    if not os.path.exists(args.entrada):
        print(f" Erro: O arquivo '{args.entrada}' não foi encontrado.")
        return

    print(f" Processando o arquivo: {args.entrada}...")

    resultado = processar_csv(args.entrada, args.saida)

    print("\n Higienização concluída com sucesso!")
    print(" Resumo:")
    print(f"   - Linhas processadas: {resultado['processadas']}")
    print(f"   - Linhas removidas: {resultado['removidas']}")
    print(f" Arquivo salvo como: {args.saida}\n")


if __name__ == "__main__":
    main()
