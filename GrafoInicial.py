# Universidad del Valle de Guatemala
# Algortimos y estructuras de datos
# Sección 100
# Proyecto 2: Sistema de recomendación
# Julio Herrera       19402
# Oliver de León      19270
# Laura Tamath        19365


import networkx as nx

def generar_grafo(tipo_coccion):
    G = nx.DiGraph()
    
# agegar nodos (20)
    G.add_node("Horno")
    G.add_node("Baño amarillo")
    G.add_node("Parrilla")
    G.add_node("Hervir")
    G.add_node("Caldo Blanco")
    G.add_node("Al vapor")
    G.add_node("Freir")
    G.add_node("Dorar")
    G.add_node("Papillote")
    G.add_node("A la sal")
    G.add_node("Gratinar")
    G.add_node("Rustir")
    G.add_node("Al vacio")
    G.add_node("Brasar")
    G.add_node("A la plancha")
    G.add_node("Escaltar")
    G.add_node("Blanqueat")
    G.add_node("Saltear")
    G.add_node("Sofreir")
    G.add_node("Guisar")
    G.add_node("Estofar")
    G.add_node("Brasear")
#print ("Nodos: ", G.nodes())

#Agregar aristas (18)
     G.add_edge("Horno","Papillote")
     G.add_edge("Horno","A la Sal")
     G.add_edge("Horno","Gratinar")
     G.add_edge("Baño Maria","Rustir")
     G.add_edge("Baño Maria","Al vacio")
     G.add_edge("Parrilla","Brasar")
     G.add_edge("Parrilla","A la plancha")
     G.add_edge("Hervir","Escaltar ")
     G.add_edge("Caldo blanco","Blanquear")
     G.add_edge("Blanquear","Brasear")
     G.add_edge("Blanquear","Guisar")
     G.add_edge("Freir","Saltear")
     G.add_edge("Dorar","Sofreir")
     G.add_edge("Dorar","Saltear")
     G.add_edge("Saltear","Guisar")
     G.add_edge("Sofreir","Brasear")
     G.add_edge("Caldo blanco","Estofar")
     G.add_edge("Hervir","Blanquear ")
     
#Orden DFS del grafo
    return (list(nx.dfs_preorder_nodes(G,tipo_coccion)))
     
    