# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

bibliotecas necessárias:
pip install pandas openpyxl xlsxwriter

"""

import pandas as pd

"""Carregar dados de um arquivo Excel para um DataFrame do pandas"""

"""def load_data(shopping_trends.csv):
    # Carregar dados do arquivo Excel
    return pd.read_csv("(2) shopping_trends.csv", sep=",", decimal=".")
"""
import pandas as pd
import os

def load_data(file_name):
    # Obter o caminho completo do arquivo
    file_path = 'C:/Users/jenif/OneDrive/Documentos/TCC/Anonimização Conjunto de Tendencias de Compras/shopping_trends.csv'  # Caminho completo do arquivo
    # Carregar dados do arquivo CSV
    return pd.read_csv(file_path, sep=",", decimal=".")

"""Função para Aplicar K-anonimato
Objetivo: Aplicar K-anonimato nos dados
Passos: 1 - Copiar os dados originais para evitar modificações diretas
        2 - Agrupar os dados pelos quasi-identificadores
        3 - Filtrar os grupos que têm pelo menos kkk registros
Resultado: Apenas os grupos que atendem ao critério de K-anonimato são mantidos
"""
def k_anonymity(data, quasi_identifiers, k):
    # Função simplificada para aplicar K-anonimato
    anonymized_data = data.copy()
    
    # Agrupar dados pelos quasi-identificadores e garantir que cada grupo tenha pelo menos k registros
    grouped_data = anonymized_data.groupby(quasi_identifiers).filter(lambda x: len(x) >= k)
    
    return grouped_data

"""Função para Aplicar i-diversidade
Objetivo: AAplicar i-diversidade nos dados
Passos: 1 - Copiar os dados originais
        2 - Definir uma função is_i_diverse para verificar se um grupo tem pelo menos lll valores distintos para o atributo sensível
        3 - Agrupar os dados pelos quasi-identificadores e filtrar os grupos que atendem à condição de i-diversidade.
Resultado: Apenas os grupos que atendem ao critério de i-diversidade são mantidos
"""

def i_diversity(data, sensitive_attribute, quasi_identifiers, l):
    # Função simplificada para aplicar i-diversidade
    anonymized_data = data.copy()
    
    def is_i_diverse(group):
        return group[sensitive_attribute].nunique() >= l
    
    # Filtrar grupos que atendem à condição de i-diversidade
    diverse_groups = anonymized_data.groupby(quasi_identifiers).filter(is_i_diverse)
    
    return diverse_groups

def save_data(data, output_file_path):
    # Salvar dados anonimizados no arquivo Excel
    data.to_excel(output_file_path, index=False)

def main():
    input_file = 'C:/Users/jenif/OneDrive/Documentos/TCC/Anonimização Conjunto de Tendencias de Compras/shopping_trends.csv'  # Substitua pelo caminho do seu arquivo de entrada
    output_file = 'anonymized_data.csv'  # Substitua pelo caminho do arquivo de saída
    quasi_identifiers = ['Age', 'Gender', 'Location', 'Category']  # Substitua pelos quasi-identificadores relevantes
    sensitive_attribute = 'Purchase Amount (USD)'  # Substitua pelo atributo sensível relevante
    k = 3  # Defina o valor de K para K-anonimato
    l = 2  # Defina o valor de L para i-diversidade

    data = load_data(input_file)
    
    # Aplicar K-anonimato
    data_k_anonymized = k_anonymity(data, quasi_identifiers, k)
    
    # Aplicar i-diversidade
    data_anonymized = i_diversity(data_k_anonymized, sensitive_attribute, quasi_identifiers, l)
    
    save_data(data_anonymized, output_file)

if __name__ == "__main__":
    main()

