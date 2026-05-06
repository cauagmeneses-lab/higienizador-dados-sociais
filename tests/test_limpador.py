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