#Algoritmo relaciones
#IDEALIZACION DE CODIGO RESPECTIVO UNION PYTHON - NEO4J
# Julio Herrera       19402
# Oliver de León      19270
# Laura Tamath        19365
#Retrieved from https://neo4j.com/developer/modeling-designs/


#DataBAse
db = GraphDatabase
#Nodos caracteristicos
caracteristica = db.labels.create("Caracteristica")
#Almacena los posibles platos
plato = db.labels.create("Plato")
#Identifica que tan gourmet es
gourmet = db.labels.create("Gourmet")

#Nodes, posibles platos
ajo= db.nodes.create(name="Ajo")
Picante= db.nodes.create(name="Picante")
Salado = db.nodes.create(name="Salado")
Dulce = db.nodes.create(name="Dulce")
Postre = db.nodes.create(name="Postre")
Barato= db.nodes.create(name="Barato")
Desayuno = db.nodes.create(name="Desayuno")
Almuerzo= db.nodes.create(name="Almuerzo")
Cena= db.nodes.create(name="Cena")
Caro= db.nodes.create(name="Caro")
Light= db.nodes.create(name="Light")
Merienda = db.nodes.create(name="Merienda")
Agrio = db.nodes.create(name="Agrio")

#Adding caracteristicas
caracteristica.add(Merienda,Picante,Salado,Dulce,Postre,Barato,Desayuno,Almuerzo,Cena,Caro)

#Generaring platos
p1 = db.nodes.create(name="Ensalada", gourmet = "5")
polique.add(p1)
#Relaciones
Cena.relationships.create(p1)
Almuerzo.relationships.create(p1)
Barato.relationships.create(p1)
light.relationships.create(p1)

#Generaring platos
p2 = db.nodes.create(name="Caldo", gourmet = "8")
polique.add(p2)
#Relaciones
Barato.relationships.create(p2)
Almuerzo.relationships.create(p2)
Salado.relationships.create(p2)


#Generaring platos
p3 = db.nodes.create(name="Spaguetti", gourmet = "7")
polique.add(p3)
#Relaciones
Caro.relationships.create(p3)
Almuerzo.relationships.create(p3)
Salado.relationships.create(p3)
Cena.relationships.create(p3)


#Generaring platos
p4 = db.nodes.create(name="Panqueques", gourmet = "10")
polique.add(p4)
#Relaciones
Barato.relationships.create(p4)
Cena.relationships.create(p4)
Merienda.relationships.create(p4)
Dulce.relationships.create(p4)

#Generaring platos
p5 = db.nodes.create(name="Pollo al limon", gourmet = "9")
polique.add(p5)
#Relaciones
Cena.relationships.create(p5)
Salado.relationships.create(p5)
Agrio.relationships.create(p5)
