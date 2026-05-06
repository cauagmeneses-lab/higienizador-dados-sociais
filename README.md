#  Higienizador de Dados Sociais

**Versão Atual:** 1.0.0
## 🚀 Deploy e Execução (Como Usar)

Por ser uma aplicação de Interface de Linha de Comando (CLI), o deploy e a execução são feitos diretamente via terminal. Siga os passos:

1. **Clone o repositório:**
   `git clone https://github.com/cauagmeneses-lab/higienizador-dados-sociais.git`
2. **Instale as dependências:**
   `pip install -r requirements.txt`
3. **Execute o programa passando o seu arquivo sujo:**
   `python src/cli.py sujo.csv`

*(Nota: A aplicação já está integrada à API pública do ViaCEP. Caso o seu arquivo possua uma coluna chamada `CEP`, o programa buscará os dados de endereço automaticamente na internet e adicionará as colunas de Logradouro, Bairro e UF no arquivo limpo).*
##  O Problema
Muitas ONGs, projetos comunitários e pesquisadores independentes lidam diariamente com listas de dados abertos (doadores, beneficiários, postos de saúde). Frequentemente, essas planilhas CSV vêm completamente despadronizadas, com linhas em branco, nomes em formatos variados e documentos/telefones contendo letras e símbolos misturados. O trabalho manual de higienizar isso consome um tempo precioso que deveria ser focado na causa social.

##  A Solução
Uma aplicação de Interface de Linha de Comando (CLI) simples e direta. O usuário fornece um arquivo CSV "sujo", e a aplicação aplica regras de higienização automatizadas (remoção de vazios, padronização de capitalização e extração de dígitos de documentos), gerando um novo arquivo CSV limpo e pronto para uso em softwares de gestão.

##  Público-Alvo
Coordenadores de ONGs, voluntários administrativos e assistentes sociais que lidam com gestão de dados, mas não possuem ferramentas caras de tratamento de dados.

##  Funcionalidades Principais
- Leitura de arquivos CSV com tolerância a codificações divergentes (`latin-1` para `utf-8`).
- Remoção automática de linhas nulas ou inválidas.
- Padronização de nomes (Title Case e remoção de espaços extras).
- Limpeza de colunas de documentos (CPF/Telefone), mantendo apenas caracteres numéricos.
- Relatório de execução direto no terminal.

##  Tecnologias Utilizadas
- **Python 3** (Linguagem Principal)
- **argparse** e **csv** (Bibliotecas Nativas Python)
- **pytest** (Testes Automatizados)
- **flake8** (Linting / Análise Estática)
- **GitHub Actions** (Integração Contínua - CI)

---

##  Instruções de Instalação e Uso

### 1. Clonar e Instalar Dependências
Certifique-se de ter o Python instalado. No seu terminal, execute:
```bash
# Clone este repositório (substitua o link pelo seu)
git clone [https://github.com/cauagmeneses-lab/higienizador-dados-sociais.git](https://github.com/Cauã_Vinícius_Venturell_de_Carvalho_Gonçalves_Meneses/higienizador-dados-sociais.git)
cd higienizador-dados-sociais

# Instale as dependências exigidas
python -m pip install -r requirements.txt