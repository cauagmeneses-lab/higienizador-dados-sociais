import re
import csv
import requests


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


def buscar_cep(cep: str) -> dict:
    """Busca dados de endereço na API pública do ViaCEP."""
    cep_limpo = limpar_documento(cep)
    if len(cep_limpo) != 8:
        return {}

    try:
        url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
        resposta = requests.get(url, timeout=5)

        if resposta.status_code == 200:
            dados = resposta.json()
            if "erro" not in dados:
                return {
                    "Logradouro": dados.get("logradouro", ""),
                    "Bairro": dados.get("bairro", ""),
                    "Localidade": dados.get("localidade", ""),
                    "UF": dados.get("uf", "")
                }
    except requests.RequestException:
        pass

    return {}


def processar_csv(caminho_entrada: str, caminho_saida: str) -> dict:
    """Aplica regras nas colunas, consome API e salva o CSV."""
    linhas_proc = 0
    linhas_rem = 0

    with open(caminho_entrada, 'r', encoding='latin-1') as arq_in:
        leitor = list(csv.DictReader(arq_in))

        if not leitor:
            return {"processadas": 0, "removidas": 0}

        campos = list(leitor[0].keys())

        if "CEP" in campos:
            colunas_extras = ["Logradouro", "Bairro", "Localidade", "UF"]
            for col in colunas_extras:
                if col not in campos:
                    campos.append(col)

        with open(caminho_saida, 'w', encoding='utf-8', newline='') as arq_out:
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

                if "CEP" in linha:
                    linha["CEP"] = limpar_documento(linha["CEP"])
                    dados_end = buscar_cep(linha["CEP"])

                    linha["Logradouro"] = dados_end.get("Logradouro", "")
                    linha["Bairro"] = dados_end.get("Bairro", "")
                    linha["Localidade"] = dados_end.get("Localidade", "")
                    linha["UF"] = dados_end.get("UF", "")

                linha.pop(None, None)
                escritor.writerow(linha)
                linhas_proc += 1

    return {"processadas": linhas_proc, "removidas": linhas_rem}