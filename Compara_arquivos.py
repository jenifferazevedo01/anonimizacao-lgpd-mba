# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 22:54:41 2024

@author: jenif
"""

import pandas as pd

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

def compare_anonymized_files(original_file, anonymized_file, quasi_identifiers, sensitive_attribute, k, l):
    # Carregar dados originais e anonimizados
    original_data = load_data(original_file)
    anonymized_data = load_data(anonymized_file)

    # Reindexar os DataFrames para garantir os mesmos índices e colunas
    original_data = original_data.reindex_like(anonymized_data)

    # Aplicar k-anonimato aos dados originais
    data_k_anonymized = k_anonymity(original_data, quasi_identifiers, k)

    # Aplicar i-diversidade aos dados k-anonimizados
    data_anonymized = i_diversity(data_k_anonymized, sensitive_attribute, quasi_identifiers, l)

    # Comparar dados anonimizados com os dados originais
    comparison_results = original_data.compare(data_anonymized)

    return comparison_results

def main():
    original_file = "C:/Users/jenif/OneDrive/Documentos/TCC/Anonimização Conjunto de Tendencias de Compras/shopping_trends.csv"
    anonymized_file = 'anonymized_data.csv'  # Arquivo anonimizado gerado pelo script anterior
    quasi_identifiers = ['Age', 'Gender', 'Location', 'Category']
    sensitive_attribute = 'Purchase Amount (USD)'
    k = 3
    l = 2

    # Comparar os arquivos anonimizados
    differences = compare_anonymized_files(original_file, anonymized_file, quasi_identifiers, sensitive_attribute, k, l)

    # Exibir as diferenças encontradas
    print("Diferenças entre os arquivos original e anonimizado:")
    print(differences)

if __name__ == "__main__":
    main()
