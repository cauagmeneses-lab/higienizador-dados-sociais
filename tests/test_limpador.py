from src.limpador import padronizar_nome, limpar_documento, linha_eh_valida, buscar_cep


def test_padronizar_nome():
    assert padronizar_nome("  joão  ") == "João"


def test_limpar_documento():
    assert limpar_documento("123.abc") == "123"


def test_linha_eh_valida():
    assert linha_eh_valida({"a": "1"}) is True
    assert linha_eh_valida({"a": ""}) is False


def test_integracao_viacep_cep_valido():
    """Testa se a API ViaCEP retorna dados corretos."""
    resultado = buscar_cep("01001-000")
    assert resultado["Logradouro"] == "Praça da Sé"
    assert resultado["Localidade"] == "São Paulo"
    assert resultado["UF"] == "SP"


def test_integracao_viacep_cep_invalido():
    """Testa se a API lida com CEP falso sem quebrar."""
    resultado = buscar_cep("00000-000")
    assert resultado == {}
    