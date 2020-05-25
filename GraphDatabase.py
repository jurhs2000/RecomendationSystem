# Proyecto Final Algoritmos y Estructura de Datos
# Base de Datos Python - NEO4J
# Oliver Josué de León Milian 19270
# Julio Roberto Saban Herrera 19XXX

from neo4j import GraphDatabase

# Python - neo4j connection is available
db = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "uvg123"),encrypted=False)
session = db.session()

# Taste label and nodes are created
a = "CREATE (A1:TASTE{name:'Spicy'}),(B1:TASTE{name:'Salty'}),(C1:TASTE{name:'Sweet'}),"
a +="(D1:TASTE{name:'Sour'}),(E1:TASTE{name:'Bitter'}),(F1:TASTE{name:'Umami'}),"

# Ingredients label and nodes are created
a += "(A:INGREDIENTS{name:'Butter'}),(B:INGREDIENTS{name:'Flour'}),(C:INGREDIENTS{name:'Ham'}),"
a +="(D:INGREDIENTS{name:'Oil'}),(E:INGREDIENTS{name:'Bacon'}),(F:INGREDIENTS{name:'Beef'}),"
a +="(G:INGREDIENTS{name:'Chicken'}),(H:INGREDIENTS{name:'Cream'}),(I:INGREDIENTS{name:'Cheese'}),"
a +="(J:INGREDIENTS{name:'Eggs'}),(K:INGREDIENTS{name:'Potato'}),(M:INGREDIENTS{name:'Milk'}),"
a +="(N:INGREDIENTS{name:'Yoghurt'}),(L:INGREDIENTS{name:'Apple'}),(O:INGREDIENTS{name:'Bread'}),"
a +="(P:INGREDIENTS{name:'Lemon'}),(Q:INGREDIENTS{name:'Sugar'}),(R:INGREDIENTS{name:'Water'}),"
a +="(S:INGREDIENTS{name:'Banana'}),(T:INGREDIENTS{name:'Strawberry'}),(U:INGREDIENTS{name:'Salmon'}),"
a +="(V:INGREDIENTS{name:'Noodles'}),(W:INGREDIENTS{name:'Pasta'}),(X:INGREDIENTS{name:'Tomato'}),"
a +="(Y:INGREDIENTS{name:'Onion'}),(Z:INGREDIENTS{name:'Lettuce'}),"

# Styles label and nodes are created
a += "(AA:STYLES{name:'Boiled'}),(AB:STYLES{name:'Baked'}),(AC:STYLES{name:'Fried'}),"
a += "(AD:STYLES{name:'Broiled'}),(AE:STYLES{name:'Gratined'}),(AF:STYLES{name:'Simmered'}),"
a += "(AG:STYLES{name:'Caramelised'}),(AH:STYLES{name:'Glaced'}),(AI:STYLES{name:'Barbecued'}),"

# Kind label and nodes are created
a += "(BA:KIND{name:'Beverage'}),(BB:KIND{name:'Dessert'}),(BC:KIND{name:'Light'}),"
a += "(BD:KIND{name:'Main_Course'}),(BE:KIND{name:'First_Course'}),"

# Meal label and nodes are created
a += "(CA:MEAL{name:'Spaghetti'}),(CB:MEAL{name:'Greek_Salad'}),(CC:MEAL{name:'French_Fries'}),"
a += "(CD:MEAL{name:'American_Hamburger'}),(CE:MEAL{name:'Strawberry_Cake'}),(CF:MEAL{name:'Sandwich'}),"
a += "(CG:MEAL{name:'American_Hamburger'}),(CH:MEAL{name:'Banana_MilkShake'}),(CI:MEAL{name:'Fruit_Juice'}),"
a += "(CJ:MEAL{name:'Cookies'}),(CK:MEAL{name:'Tomato_Soup'}),(CM:MEAL{name:'Mashed_Potatoes'}),"
a += "(CN:MEAL{name:'Salmon'}),(CL:MEAL{name:'Broiled_Chicken'}),(CO:MEAL{name:'Tacos'}),"
a += "(CP:MEAL{name:'Italian_Pizza'}),(CQ:MEAL{name:'Rice_Noodles'}),(CR:MEAL{name:'Sushi'}),"
a += "(CS:MEAL{name:'Cocktails'}),(CT:MEAL{name:'Tossed_Salad'}),(CU:MEAL{name:'Meatballs'}),"
a += "(CV:MEAL{name:'Lemonade'}),(CW:MEAL{name:'Mac&Cheese'}),(CX:MEAL{name:'Chicken_Soup'}),"
a += "(CY:MEAL{name:'SantaFe_Salad'}),(CZ:MEAL{name:'Pancakes'}),(CZA:MEAL{name:'Onion_Rings'})"



nodes = a
session.run(nodes)

db.close()
