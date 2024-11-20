import pandas as pd
import pyautogui
import time
from datetime import datetime
import webbrowser
import os

class AutomacaoCadastroFuncionarios:
    def __init__(self, arquivo_excel: str):
        self.dados = pd.read_excel(arquivo_excel)
        pyautogui.PAUSE = 0.5  # Pausa entre ações

    def abrir_site(self, caminho_html):
        arquivo_url = 'file://' + os.path.abspath(caminho_html)
        webbrowser.open(arquivo_url)
        time.sleep(2)

    def processar_cadastros(self):
        print(f"Iniciando cadastro de {len(self.dados)} funcionários...")

        campos = {
            'nome': None,
            'cargo': None,
            'departamento': None,
            'salario': None,
            'data_admissao': None,
            'botao_cadastrar': None
        }

        print("\nVamos calibrar as posições dos campos.")
        for campo in campos:
            input(f"Posicione o mouse no campo '{campo}' e pressione Enter...")
            campos[campo] = pyautogui.position()
            print(f"Posição de '{campo}' registrada: {campos[campo]}")

        for idx, funcionario in self.dados.iterrows():
            print(f"\nProcessando funcionário {idx + 1}/{len(self.dados)}")

            for campo, coords in campos.items():
                if campo != 'botao_cadastrar':
                    pyautogui.moveTo(coords)
                    pyautogui.click()
                    pyautogui.hotkey('ctrl', 'a')

                    if campo == 'salario':
                        valor = str(funcionario[campo])
                    elif campo == 'data_admissao':
                        valor = funcionario[campo].strftime('%d%m%Y')
                    else:
                        valor = str(funcionario[campo])

                    pyautogui.typewrite(valor)
                    time.sleep(0.3)

            pyautogui.moveTo(campos['botao_cadastrar'])
            pyautogui.click()
            time.sleep(0.5)

            print(f"Funcionário {idx + 1} cadastrado com sucesso!")

        print("\nProcessamento finalizado!")

def main():
    print("Gerando dados de teste...")
    from gerador_dados import gerar_dados_teste
    arquivo_excel = gerar_dados_teste()

    arquivo_html = 'cadastro_funcionarios.html'

    try:
        automacao = AutomacaoCadastroFuncionarios(arquivo_excel)

        print("\nAbrindo página de cadastro...")
        automacao.abrir_site(arquivo_html)

        input("\nPressione Enter quando a página estiver carregada para iniciar o cadastro...")
        automacao.processar_cadastros()

    except Exception as e:
        print(f"Erro durante a execução: {str(e)}")

if __name__ == "__main__":
    main()
