# -*- coding: utf-8 -*-
"""
Created on Tue Jun 03 18:40:27 2024

@author: jeniffer rodrigues
"""

import pandas as pd

def load_data(file_path):
    # Carregar dados do arquivo CSV
    return pd.read_csv(file_path, sep=",", decimal=".")

def k_anonymity(data, quasi_identifiers, k):
    grouped_data = data.groupby(quasi_identifiers, as_index=False)
    # Agregar os dados para garantir que cada grupo tenha pelo menos k linhas
    grouped_data_filtered = grouped_data.filter(lambda x: len(x) >= k)
    # Restaurar o DataFrame original, incluindo todas as linhas dos grupos mantidos
    return data[data.index.isin(grouped_data_filtered.index)]

def i_diversity(data, sensitive_attribute, quasi_identifiers, l):
    grouped_data = data.groupby(quasi_identifiers, as_index=False)
    
    def is_i_diverse(group):
        return group[sensitive_attribute].nunique() >= l
    
    # Filtrar grupos que atendem ao critério de diversidade
    diverse_groups = grouped_data.filter(lambda x: is_i_diverse(x))
    # Restaurar o DataFrame original, incluindo todas as linhas dos grupos mantidos
    return data[data.index.isin(diverse_groups.index)]

def save_data(data, output_file_path):
    # Salvar dados anonimizados no arquivo CSV
    data.to_csv(output_file_path, index=False, sep=",", decimal=".")

def main():
    input_file = "C:/Users/jenif/OneDrive/Documentos/TCC/Anonimização Conjunto de Tendencias de Compras/shopping_trends.csv"
    output_file = 'shopping_trends_anonimizados.csv'  # Caminho fixo do arquivo de saída
    quasi_identifiers = ['Age', 'Location', 'Category']
    sensitive_attribute = 'Gender'
    k = 3
    l = 2

    data = load_data(input_file)
    
    data_k_anonymized = k_anonymity(data, quasi_identifiers, k)
    
    data_anonymized = i_diversity(data_k_anonymized, sensitive_attribute, quasi_identifiers, l)
    
    save_data(data_anonymized, output_file)

if __name__ == "__main__":
    main()
