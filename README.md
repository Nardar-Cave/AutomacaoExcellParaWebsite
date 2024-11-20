# 🤖 Automação de Cadastro de Funcionários

## 📝 Descrição do Projeto
Este projeto é uma solução de automação para cadastro de funcionários, desenvolvido em Python. O sistema gera dados fictícios de funcionários, e os usa em um site de exemplo e utiliza automação de interface para preencher formulários automaticamente.

## ✨ Características do Projeto

### 🗂️ Componentes
- **Site de Cadastro**: Interface web simples para cadastro de funcionários
- **Gerador de Dados**: Script para criar planilha Excel com dados aleatórios
- **Automação**: Script que preenche o formulário automaticamente

### 📚 Bibliotecas Utilizadas
- `pandas`: Manipulação de dados e criação de planilhas Excel
- `pyautogui`: Automação de interface gráfica (movimentação do mouse, digitação)
- `openpyxl`: Suporte para leitura/escrita de arquivos Excel
- `datetime`: Geração de datas aleatórias
- `webbrowser`: Abertura automática de páginas web
- `random`: Geração de dados aleatórios

### 🛠️ Funcionalidades
- Geração automática de dados de funcionários
- Criação de planilha Excel com informações fictícias
- Cadastro automático em formulário web
- Calibração interativa das posições dos campos

## 🚀 Como Usar o Projeto

### Pré-requisitos
- Python 3.8+
- Pip (gerenciador de pacotes)

### Instalação
1. Clone o repositório:
```bash
git clone https://github.com/Nardar-Cave/AutomacaoExcellParaWebsite.git
cd automacao-cadastro
```

2. Instale as dependências:
```bash
pip install pandas pyautogui openpyxl
```

### Execução
1. Execute o script principal:
```bash
python automacao_cadastro.py
```

### 🎯 Processo de Calibração
- Mantenha o terminal do VSCode aberto
- O script solicitará que você posicione o mouse em cada campo
- Para cada campo solicitado:
  1. Mova o cursor do mouse para o campo desejado
  2. Pressione Enter no terminal
  3. O script registrará as coordenadas

## 👍 Pontos Positivos
- Totalmente automatizado
- Geração de dados realista
- Interface de calibração simples
- Flexível para diferentes formulários
- Código modular

## 👎 Limitações Atuais
- Dependente de posicionamento fixo dos elementos
- Requer intervenção manual para calibração
- Não funciona com páginas web dinâmicas
- Sensível a mudanças na interface

## 🔮 Futuras Melhorias
- [ ] Implementar interface gráfica (GUI)
- [ ] Adicionar suporte a seletores CSS/XPath
- [ ] Integração com Selenium para web scraping
- [ ] Tratamento de erros mais robusto
- [ ] Suporte para múltiplos navegadores
- [ ] Modo de gravação de macros

## ⚠️ Avisos Importantes
- Teste em um ambiente controlado
- Verifique as coordenadas antes de cada execução
- Mantenha o mouse livre durante a execução
- Tenha sempre um método de interrupção (Ctrl+C)

## 🤝 Contribuições
Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request.
