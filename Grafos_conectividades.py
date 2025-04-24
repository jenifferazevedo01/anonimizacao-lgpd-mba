# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 12:12:49 2025

@author: jeniffer rodrigues
"""

import networkx as nx
import matplotlib.pyplot as plt

# Dados simulando conexões entre registros antes da anonimização
conexoes_antes = [('R1', 'R2'), ('R1', 'R4'), ('R2', 'R4'), ('R2', 'R10'), 
                  ('R10', 'R9'), ('R5', 'R6'), ('R5', 'R8'), ('R3', 'R7')]

# Dados simulando conexões após anonimização (menos relações diretas)
conexoes_depois = [('R1', 'R4'), ('R2', 'R4'), ('R3', 'R7'), ('R5', 'R6')]

# Criar grafos
G_antes = nx.Graph()
G_antes.add_edges_from(conexoes_antes)

G_depois = nx.Graph()
G_depois.add_edges_from(conexoes_depois)

# Layout fixo para consistência entre os dois grafos
pos_antes = nx.spring_layout(G_antes, seed=42)
pos_depois = nx.spring_layout(G_depois, seed=42)

# Criar a figura
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Grafo antes da anonimização
nx.draw(G_antes, pos_antes, ax=axs[0], with_labels=True, node_color='skyblue',
        node_size=1500, edge_color='gray')
axs[0].set_title('Antes da Anonimização')
axs[0].grid(True)

# Grafo depois da anonimização
nx.draw(G_depois, pos_depois, ax=axs[1], with_labels=True, node_color='lightgreen',
        node_size=1500, edge_color='gray')
axs[1].set_title('Depois da Anonimização')
axs[1].grid(True)

plt.tight_layout()
plt.show()