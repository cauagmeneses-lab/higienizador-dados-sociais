from src.limpador import padronizar_nome, limpar_documento, linha_eh_valida


def test_padronizar_nome_caminho_feliz():

    assert padronizar_nome("  joão   da silva  ") == "João Da Silva"


def test_padronizar_nome_caso_limite():

    assert padronizar_nome("") == ""


def test_limpar_documento_caminho_feliz():

    assert limpar_documento("123.456.789-00") == "12345678900"


def test_limpar_documento_entrada_invalida():

    assert limpar_documento("(11) 9876A-4321") == "1198764321"


def test_linha_valida_com_dados():
    linha = {"Nome": "Maria", "CPF": ""}
    assert linha_eh_valida(linha) is True


def test_linha_invalida_totalmente_vazia():

    linha = {"Nome": "   ", "CPF": ""}
    assert linha_eh_valida(linha) is False
