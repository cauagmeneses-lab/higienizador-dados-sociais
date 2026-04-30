import re
import csv


def padronizar_nome(nome: str) -> str:
    """Remove espaços extras e capitaliza."""
    if not nome:
        return ""
    nome_limpo = " ".join(nome.split())
    return nome_limpo.title()


def limpar_documento(documento: str) -> str:
    """Remove tudo que não for número."""
    if not documento:
        return ""
    return re.sub(r'[^\d]', '', str(documento))


def linha_eh_valida(linha: dict) -> bool:
    """Verifica se a linha tem dados úteis."""
    for valor in linha.values():
        if valor and str(valor).strip():
            return True
    return False


def processar_csv(caminho_entrada: str, caminho_saida: str) -> dict:
    """Aplica regras nas colunas e salva o CSV limpo."""
    linhas_proc = 0
    linhas_rem = 0

    with open(caminho_entrada, 'r', encoding='latin-1') as arq_in, \
            open(caminho_saida, 'w', encoding='utf-8', newline='') as arq_out:

        leitor = csv.DictReader(arq_in)
        campos = leitor.fieldnames

        if not campos:
            return {"processadas": 0, "removidas": 0}

        escritor = csv.DictWriter(arq_out, fieldnames=campos)
        escritor.writeheader()

        for linha in leitor:
            if not linha_eh_valida(linha):
                linhas_rem += 1
                continue

            if "Nome" in linha:
                linha["Nome"] = padronizar_nome(linha["Nome"])

            if "CPF" in linha:
                linha["CPF"] = limpar_documento(linha["CPF"])

            if "Telefone" in linha:
                linha["Telefone"] = limpar_documento(linha["Telefone"])

            linha.pop(None, None)

            escritor.writerow(linha)
            linhas_proc += 1

    return {"processadas": linhas_proc, "removidas": linhas_rem}
