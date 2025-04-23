# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 22:43:24 2024

@author: jenif
"""

import pandas as pd
import os

def load_data(file_path):
    # Carregar dados do arquivo CSV
    return pd.read_csv(file_path, sep=",", decimal=".")

def k_anonymity(data, quasi_identifiers, k):
    anonymized_data = data.copy()
    grouped_data = anonymized_data.groupby(quasi_identifiers).filter(lambda x: len(x) >= k)
    return grouped_data

def i_diversity(data, sensitive_attribute, quasi_identifiers, l):
    anonymized_data = data.copy()
    
    def is_i_diverse(group):
        return group[sensitive_attribute].nunique() >= l
    
    diverse_groups = anonymized_data.groupby(quasi_identifiers).filter(is_i_diverse)
    return diverse_groups

def save_data(data, output_file_path):
    # Salvar dados anonimizados no arquivo CSV
    data.to_csv(output_file_path, index=False, sep=",", decimal=".")

def compare_first_rows(original_data, anonymized_data):
    # Exibir as 5 primeiras linhas do arquivo original
    print("Primeiras 5 linhas do arquivo original:")
    print(original_data.head())

    # Exibir as 5 primeiras linhas do arquivo anonimizado
    print("\nPrimeiras 5 linhas do arquivo anonimizado:")
    print(anonymized_data.head())

    # Comparar e mostrar diferenças
    print("\nDiferenças entre as primeiras 5 linhas:")
    diff = original_data.head().compare(anonymized_data.head())
    print(diff)

def main():
    input_file = "C:/Users/jenif/OneDrive/Documentos/TCC/Anonimização Conjunto de Tendencias de Compras/shopping_trends.csv"
    output_file = 'anonymized_data.csv'  # Caminho fixo do arquivo de saída
    quasi_identifiers = ['Age', 'Gender', 'Location', 'Category']
    sensitive_attribute = 'Purchase Amount (USD)'
    k = 3
    l = 2

    # Carregar dados originais
    original_data = load_data(input_file)
    
    # Anonimizar dados
    data_k_anonymized = k_anonymity(original_data, quasi_identifiers, k)
    data_anonymized = i_diversity(data_k_anonymized, sensitive_attribute, quasi_identifiers, l)
    
    # Salvar dados anonimizados
    save_data(data_anonymized, output_file)

    # Comparar as primeiras 5 linhas
    compare_first_rows(original_data, data_anonymized)

if __name__ == "__main__":
    main()
