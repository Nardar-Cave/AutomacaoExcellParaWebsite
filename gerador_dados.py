import pandas as pd
import random
from datetime import datetime, timedelta
import numpy as np

def gerar_dados_teste(num_registros=20):
    nomes = ['João Silva', 'Maria Santos', 'Pedro Oliveira', 'Ana Costa', 'Carlos Souza',
             'Paula Martins', 'Lucas Ferreira', 'Julia Lima', 'Marcos Rodrigues', 'Beatriz Alves']

    cargos = ['Analista', 'Desenvolvedor', 'Gerente', 'Coordenador', 'Assistente',
              'Supervisor', 'Técnico', 'Consultor', 'Especialista', 'Diretor']

    departamentos = ['TI', 'RH', 'Financeiro', 'Marketing', 'Vendas',
                    'Operações', 'Administrativo', 'Jurídico', 'Comercial', 'Suporte']

    dados = {
        'nome': [random.choice(nomes) for _ in range(num_registros)],
        'cargo': [random.choice(cargos) for _ in range(num_registros)],
        'departamento': [random.choice(departamentos) for _ in range(num_registros)],
        'salario': [round(random.uniform(3000, 15000), 2) for _ in range(num_registros)],
        'data_admissao': [
            (datetime.now() - timedelta(days=random.randint(0, 365*2))).strftime('%Y-%m-%d')
            for _ in range(num_registros)
        ]
    }

    # Criar DataFrame
    df = pd.DataFrame(dados)

    # Salvar em Excel
    nome_arquivo = 'dados_funcionarios.xlsx'
    df.to_excel(nome_arquivo, index=False)
    print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")
    return nome_arquivo

if __name__ == "__main__":
    arquivo = gerar_dados_teste()
