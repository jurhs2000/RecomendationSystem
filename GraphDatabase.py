# Proyecto Final Algoritmos y Estructura de Datos
# Base de Datos Python - NEO4J
# Oliver Josué de León Milian 19270
# Julio Roberto Herrera Saban 19XXX
# In collaboration with Laura Tamath 19365

from neo4j import GraphDatabase

# Python - neo4j connection is available
db = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "uvg123"),encrypted=False)
session = db.session()

# Taste label and nodes are created
a =  "CREATE (SPICY:TASTE{name:'Spicy'}),(SALTY:TASTE{name:'Salty'}),(SWEET:TASTE{name:'Sweet'}),"
a += "(SOUR:TASTE{name:'Sour'}),(BITTER:TASTE{name:'Bitter'}),(UMAMI:TASTE{name:'Umami'}),"

# Ingredients label and nodes are created
a += "(BUTTER:INGREDIENTS{name:'Butter'}),(FLOUR:INGREDIENTS{name:'Flour'}),(HAM:INGREDIENTS{name:'Ham'}),"
a += "(OIL:INGREDIENTS{name:'Oil'}),(BACON:INGREDIENTS{name:'Bacon'}),(BEEF:INGREDIENTS{name:'Beef'}),"
a += "(CHICKEN:INGREDIENTS{name:'Chicken'}),(CREAM:INGREDIENTS{name:'Cream'}),(CHEESE:INGREDIENTS{name:'Cheese'}),"
a += "(EGGS:INGREDIENTS{name:'Eggs'}),(POTATO:INGREDIENTS{name:'Potato'}),(MILK:INGREDIENTS{name:'Milk'}),"
a += "(SALT:INGREDIENTS{name:'Salt'}),(APPLE:INGREDIENTS{name:'Apple'}),(BREAD:INGREDIENTS{name:'Bread'}),"
a += "(LEMON:INGREDIENTS{name:'Lemon'}),(SUGAR:INGREDIENTS{name:'Sugar'}),(WATER:INGREDIENTS{name:'Water'}),"
a += "(BANANA:INGREDIENTS{name:'Banana'}),(STRAWBERRY:INGREDIENTS{name:'Strawberry'}),(SALMON:INGREDIENTS{name:'Salmon'}),"
a += "(NOODLES:INGREDIENTS{name:'Noodles'}),(PASTA:INGREDIENTS{name:'Pasta'}),(TOMATO:INGREDIENTS{name:'Tomato'}),"
a += "(ONION:INGREDIENTS{name:'Onion'}),(LETTUCE:INGREDIENTS{name:'Lettuce'}),"

# Styles label and nodes are created
a += "(BOILED:STYLES{name:'Boiled'}),(BAKED:STYLES{name:'Baked'}),(FRIED:STYLES{name:'Fried'}),"
a += "(BROILED:STYLES{name:'Broiled'}),(GRATINED:STYLES{name:'Gratined'}),(SIMMERED:STYLES{name:'Simmered'}),"
a += "(CARAMELISED:STYLES{name:'Caramelised'}),(GLACED:STYLES{name:'Glaced'}),(BARBECUED:STYLES{name:'Barbecued'}),"

# Kind label and nodes are created
a += "(BEVERAGE:KIND{name:'Beverage'}),(DESSERT:KIND{name:'Dessert'}),(LIGHT:KIND{name:'Light'}),"
a += "(MAINCOURSE:KIND{name:'Main_Course'}),(FIRSTCOURSE:KIND{name:'First_Course'}),"

# Meal label and nodes are created
a += "(SPAGHETTI:MEAL{name:'Spaghetti'}),(GREEKSALAD:MEAL{name:'Greek_Salad'}),(FRENCHFRIES:MEAL{name:'French_Fries'}),"
a += "(AMERICANHAMBURGER:MEAL{name:'American_Hamburger'}),(STRAWBERRYCAKE:MEAL{name:'Strawberry_Cake'}),(SANDWICH:MEAL{name:'Sandwich'}),"
a += "(CLASSICHAMBURGER:MEAL{name:'Classic_Hamburger'}),(BANANAMILKSHAKE:MEAL{name:'Banana_MilkShake'}),(FRUITJUICE:MEAL{name:'Fruit_Juice'}),"
a += "(COOKIES:MEAL{name:'Cookies'}),(TOMATOSOUP:MEAL{name:'Tomato_Soup'}),(MASHEDPOTATOES:MEAL{name:'Mashed_Potatoes'}),"
a += "(SALMONMEAL:MEAL{name:'Salmon_Meal'}),(BROILEDCHICKEN:MEAL{name:'Broiled_Chicken'}),(TACOS:MEAL{name:'Tacos'}),"
a += "(ITALIANPIZZA:MEAL{name:'Italian_Pizza'}),(RICENOODLES:MEAL{name:'Rice_Noodles'}),(SUSHI:MEAL{name:'Sushi'}),"
a += "(COCKTAILS:MEAL{name:'Cocktails'}),(TOSSEDSALAD:MEAL{name:'Tossed_Salad'}),(MEATBALLS:MEAL{name:'Meatballs'}),"
a += "(LEMONADE:MEAL{name:'Lemonade'}),(MACNCHEESE:MEAL{name:'Mac&Cheese'}),(CHICKENSOUP:MEAL{name:'Chicken_Soup'}),"
a += "(SANTAFESALAD:MEAL{name:'SantaFe_Salad'}),(PANCAKES:MEAL{name:'Pancakes'}),(ONIONRINGS:MEAL{name:'Onion_Rings'}),"


#Spaghetti Relationships
a += "(SPAGHETTI)-[A:IS_A]->(MAINCOURSE),(SPAGHETTI)-[B:USE]->(PASTA),(SPAGHETTI)-[C:USE]->(OIL),(SPAGHETTI)-[D:USE]->(TOMATO),"
a += "(SPAGHETTI)-[E:USE]->(ONION),(SPAGHETTI)-[F:USE]->(WATER),(SPAGHETTI)-[G:METHOD]->(BOILED),(SPAGHETTI)-[H:TASTE]->(SALTY),"
a += "(SPAGHETTI)-[I:TASTE]->(UMAMI),(SPAGHETTI)-[J:TASTE]->(SOUR),(SPAGHETTI)-[K:METHOD]->(GRATINED),"

#Greek Salad Relationships
a += "(GREEKSALAD)-[A1:IS_A]->(MAINCOURSE),(GREEKSALAD)-[B1:IS_A]->(FIRSTCOURSE),(GREEKSALAD)-[B1100:IS_A]->(LIGHT),(GREEKSALAD)-[C1:USE]->(LETTUCE),"
a += "(GREEKSALAD)-[E1:USE]->(CHICKEN),(GREEKSALAD)-[D1:USE]->(BREAD),(GREEKSALAD)-[F1:USE]->(CHEESE),(GREEKSALAD)-[G1:TASTE]->(SALTY),"
a += "(GREEKSALAD)-[H1:TASTE]->(UMAMI),"

#French Fries Relationships
a += "(FRENCHFRIES)-[A2:IS_A]->(FIRSTCOURSE),(FRENCHFRIES)-[B2:USE]->(POTATO),(FRENCHFRIES)-[C2:USE]->(OIL),"
a += "(FRENCHFRIES)-[D2:TASTE]->(SALTY),(FRENCHFRIES)-[E2:TASTE]->(UMAMI),(FRENCHFRIES)-[F2:METHOD]->(FRIED),"

#American Hamburger Relationships
a += "(AMERICANHAMBURGER)-[A3:IS_A]->(MAINCOURSE),(AMERICANHAMBURGER)-[B3:USE]->(BREAD),(AMERICANHAMBURGER)-[C3:USE]->(LETTUCE),"
a += "(AMERICANHAMBURGER)-[D3:USE]->(CHEESE),(AMERICANHAMBURGER)-[E300:USE]->(BEEF),(AMERICANHAMBURGER)-[E3:USE]->(BACON),"
a += "(AMERICANHAMBURGER)-[F3:USE]->(TOMATO),(AMERICANHAMBURGER)-[G3:USE]->(ONION),(AMERICANHAMBURGER)-[H3:TASTE]->(UMAMI),"
a += "(AMERICANHAMBURGER)-[I3:TASTE]->(SALTY),(FRENCHFRIES)-[J3:METHOD]->(BROILED),"

#Strawberry Cake Relationships
a += "(STRAWBERRYCAKE)-[A4:IS_A]->(DESSERT),(STRAWBERRYCAKE)-[B4:USE]->(FLOUR),(STRAWBERRYCAKE)-[C4:USE]->(MILK),"
a += "(STRAWBERRYCAKE)-[D4:USE]->(STRAWBERRY),(STRAWBERRYCAKE)-[E4:USE]->(SUGAR),(STRAWBERRYCAKE)-[F4:USE]->(CREAM),"
a += "(STRAWBERRYCAKE)-[G4:USE]->(BUTTER),(STRAWBERRYCAKE)-[H4:USE]->(EGGS),(STRAWBERRYCAKE)-[I4:METHOD]->(BAKED),"
a += "(STRAWBERRYCAKE)-[J4:TASTE]->(SWEET),"

#Sandwich Relationships
a += "(SANDWICH)-[A5:IS_A]->(MAINCOURSE),(SANDWICH)-[B5:IS_A]->(LIGHT),(SANDWICH)-[C5:USE]->(BREAD),(SANDWICH)-[D5:USE]->(LETTUCE),"
a += "(SANDWICH)-[E5:USE]->(HAM),(SANDWICH)-[F5:USE]->(CHEESE),(SANDWICH)-[G5:USE]->(TOMATO),(SANDWICH)-[H5:TASTE]->(UMAMI),"

#Classic Hamburger Relationships
a += "(CLASSICHAMBURGER)-[A6:IS_A]->(MAINCOURSE),(CLASSICHAMBURGER)-[B6:USE]->(BREAD),(CLASSICHAMBURGER)-[C6:USE]->(CHICKEN),"
a += "(CLASSICHAMBURGER)-[D6:USE]->(LETTUCE),(CLASSICHAMBURGER)-[E6:USE]->(TOMATO),(CLASSICHAMBURGER)-[F6:METHOD]->(BROILED),"
a += "(CLASSICHAMBURGER)-[G6:TASTE]->(UMAMI),"

#Banana MilkShake Relationships
a += "(BANANAMILKSHAKE)-[A7:IS_A]->(BEVERAGE),(BANANAMILKSHAKE)-[B7:USE]->(MILK),(BANANAMILKSHAKE)-[C7:USE]->(BANANA),"
a += "(BANANAMILKSHAKE)-[D7:USE]->(SUGAR),(BANANAMILKSHAKE)-[E7:TASTE]->(SWEET),"

#Fruit Juice Relationships
a += "(FRUITJUICE)-[A8:IS_A]->(BEVERAGE),(FRUITJUICE)-[B8:USE]->(WATER),(FRUITJUICE)-[C8:USE]->(STRAWBERRY),"
a += "(FRUITJUICE)-[D8:USE]->(APPLE),(FRUITJUICE)-[E8:USE]->(SUGAR),(FRUITJUICE)-[F8:USE]->(BANANA),(FRUITJUICE)-[G8:TASTE]->(SWEET),"

#Cookies Relationships
a += "(COOKIES)-[A9:IS_A]->(DESSERT),(COOKIES)-[B9:USE]->(BUTTER),(COOKIES)-[C9:USE]->(SUGAR),(COOKIES)-[D9:TASTE]->(SWEET),"
a += "(COOKIES)-[E9:USE]->(MILK),(COOKIES)-[F9:USE]->(FLOUR),(COOKIES)-[G9:USE]->(EGGS),(COOKIES)-[D900:METHOD]->(BAKED),"

#Tomato Soup Relationship
a += "(TOMATOSOUP)-[A10:IS_A]->(MAINCOURSE),(TOMATOSOUP)-[B10:IS_A]->(FIRSTCOURSE),(TOMATOSOUP)-[C10:IS_A]->(LIGHT),"
a += "(TOMATOSOUP)-[D10:TASTE]->(UMAMI),(TOMATOSOUP)-[E10:TASTE]->(SOUR),(TOMATOSOUP)-[F10:USE]->(TOMATO),(TOMATOSOUP)-[G10:USE]->(WATER),"
a += "(TOMATOSOUP)-[H10:USE]->(SALT),(TOMATOSOUP)-[I10:METHOD]->(BOILED),"

#Mashed Potatoes Relationships
a += "(MASHEDPOTATOES)-[A11:IS_A]->(MAINCOURSE),(MASHEDPOTATOES)-[B11:IS_A]->(FIRSTCOURSE),(TOMATOSOUP)-[C11:IS_A]->(LIGHT),"
a += "(MASHEDPOTATOES)-[D11:TASTE]->(UMAMI),(MASHEDPOTATOES)-[E11:TASTE]->(SALTY),(TOMATOSOUP)-[F11:USE]->(TOMATO),"
a += "(MASHEDPOTATOES)-[G11:USE]->(MILK),(MASHEDPOTATOES)-[H11:USE]->(POTATO),(MASHEDPOTATOES)-[I11:USE]->(SALT),"
a += "(MASHEDPOTATOES)-[J11:METHOD]->(BOILED),"

#Salmon Meal Relationships
a += "(SALMONMEAL)-[A12:IS_A]->(MAINCOURSE),(SALMONMEAL)-[B12:IS_A]->(LIGHT),(SALMONMEAL)-[C12:TASTE]->(SALTY),"
a += "(SALMONMEAL)-[D12:TASTE]->(BITTER),(SALMONMEAL)-[E12:USE]->(SALMON),(SALMONMEAL)-[F12:USE]->(SALT),"
a += "(SALMONMEAL)-[G12:USE]->(ONION),(SALMONMEAL)-[H12:USE]->(LEMON),(SALMONMEAL)-[I12:TASTE]->(SOUR),"
a += "(SALMONMEAL)-[J12:METHOD]->(FRIED),(SALMONMEAL)-[K12:METHOD]->(BOILED),(SALMONMEAL)-[M12:METHOD]->(SIMMERED),"

#Broiled Chicken Relationships
a += "(BROILEDCHICKEN)-[A13:IS_A]->(MAINCOURSE),(BROILEDCHICKEN)-[B130:TASTE]->(SALTY),(BROILEDCHICKEN)-[C13:USE]->(CHICKEN),"
a += "(BROILEDCHICKEN)-[D13:USE]->(SALT),(BROILEDCHICKEN)-[D1300:USE]->(LEMON),(BROILEDCHICKEN)-[B13:TASTE]->(SOUR),"
a += "(BROILEDCHICKEN)-[B1300:METHOD]->(BROILED),"

#Tacos Relationships
a += "(TACOS)-[A14:IS_A]->(MAINCOURSE),(TACOS)-[B14:IS_A]->(FIRSTCOURSE),(TACOS)-[C14:TASTE]->(SALTY),(TACOS)-[D14:USE]->(CHICKEN),"
a += "(TACOS)-[E14:USE]->(ONION),(TACOS)-[F14:USE]->(TOMATO),(TACOS)-[G14:USE]->(LEMON),(TACOS)-[H14:USE]->(BEEF),"
a += "(TACOS)-[I14:USE]->(SALT),(TACOS)-[J14:METHOD]->(BROILED),"

#Italian Pizza Relationships
a += "(ITALIANPIZZA)-[A15:IS_A]->(MAINCOURSE),(ITALIANPIZZA)-[B15:TASTE]->(SALTY),(ITALIANPIZZA)-[C15:TASTE]->(UMAMI),"
a += "(ITALIANPIZZA)-[D15:USE]->(TOMATO),(ITALIANPIZZA)-[E15:USE]->(FLOUR),(ITALIANPIZZA)-[F15:USE]->(HAM),"
a += "(ITALIANPIZZA)-[G15:USE]->(CHEESE),(ITALIANPIZZA)-[H15:USE]->(ONION),(ITALIANPIZZA)-[I15:METHOD]->(BAKED),"

#Rice Noodles Relationships
a += "(RICENOODLES)-[A16:IS_A]->(MAINCOURSE),(RICENOODLES)-[B16:TASTE]->(SALTY),(RICENOODLES)-[C16:USE]->(NOODLES),"
a += "(RICENOODLES)-[D16:USE]->(WATER),(RICENOODLES)-[E16:METHOD]->(BOILED),"

#Onion Rings Relationships
a += "(ONIONRINGS)-[A17:IS_A]->(FIRSTCOURSE),(ONIONRINGS)-[B17:USE]->(CHEESE),(ONIONRINGS)-[C17:USE]->(BREAD),"
a += "(ONIONRINGS)-[D17:USE]->(EGGS),(ONIONRINGS)-[E17:USE]->(OIL),(ONIONRINGS)-[F17:USE]->(BUTTER),"
a += "(ONIONRINGS)-[G17:TASTE]->(SALTY),"

#Pancakes relationships
a += "(PANCAKES)-[A18:IS_A]->(DESSERT),(PANCAKES)-[B18:USE]->(BUTTER),(PANCAKES)-[C18:USE]->(FLOUR),"
a += "(PANCAKES)-[D18:USE]->(EGGS),(PANCAKES)-[E18:USE]->(BANANA),(PANCAKES)-[F18:USE]->(MILK),"
a += "(PANCAKES)-[G18:TASTE]->(SWEET),"

#Santa Fe Salad Relationships
a += "(SANTAFESALAD)-[A19:IS_A]->(LIGHT),(SANTAFESALAD)-[B19:USE]->(OIL),(SANTAFESALAD)-[C19:USE]->(CHICKEN),"
a += "(SANTAFESALAD)-[D19:USE]->(LETTUCE),(SANTAFESALAD)-[E19:USE]->(ONION),(SANTAFESALAD)-[F19:USE]->(TOMATO),"
a += "(SANTAFESALAD)-[G19:TASTE]->(UMAMI),"

#Chicken Soup Relationships
a += "(CHICKENSOUP)-[A20:IS_A]->(FIRSTCOURSE),(CHICKENSOUP)-[B20:USE]->(CHICKEN),(CHICKENSOUP)-[C20:USE]->(ONION),"
a += "(CHICKENSOUP)-[D20:USE]->(MILK),"
a += "(CHICKENSOUP)-[E20:TASTE]->(SPICY),(CHICKENSOUP)-[F20:TASTE]->(SALTY),"

#Mac&Cheese Relationships
a += "(MACNCHEESE)-[A21:IS_A]->(MAINCOURSE),(MACNCHEESE)-[B21:USE]->(CHEESE),(MACNCHEESE)-[C21:USE]->(NOODLES),"
a += "(MACNCHEESE)-[D21:USE]->(BUTTER),(MACNCHEESE)-[E21:USE]->(FLOUR),(MACNCHEESE)-[F21:USE]->(MILK),(MACNCHEESE)-[G21:USE]->(BREAD),"
a += "(MACNCHEESE)-[H21:TASTE]->(UMAMI),(MACNCHEESE)-[I21:TASTE]->(SALTY),"

#Lemonade Relationships
a += "(LEMONADE)-[A22:IS_A]->(BEVERAGE),(LEMONADE)-[B22:USE]->(SUGAR),(LEMONADE)-[C22:USE]->(LEMON),"
a += "(LEMONADE)-[D22:USE]->(WATER),"
a += "(LEMONADE)-[E22:TASTE]->(SWEET),"


#Meatballs Relationships
a += "(MEATBALLS)-[A23:IS_A]->(MAINCOURSE),(MEATBALLS)-[B23:USE]->(EGGS),(MEATBALLS)-[C23:USE]->(TOMATO),"
a += "(MEATBALLS)-[D23:USE]->(MILK),(MEATBALLS)-[E23:USE]->(BEEF),(MEATBALLS)-[F23:USE]->(NOODLES ),(MEATBALLS)-[G23:USE]->(CHEESE),"
a += "(MEATBALLS)-[H23:TASTE]->(SALTY),"

#Tossed Salad Relationships
a += "(TOSSEDSALAD)-[A24:IS_A]->(LIGHT),(TOSSEDSALAD)-[B24:USE]->(LETTUCE),(TOSSEDSALAD)-[C24:USE]->(TOMATO),"
a += "(TOSSEDSALAD)-[C2400:USE]->(ONION),(TOSSEDSALAD)-[D24:USE]->(OIL),(TOSSEDSALAD)-[E24:USE]->(LEMON),"
a += "(TOSSEDSALAD)-[F24:TASTE]->(UMAMI),"

#Cocktails Relationships lo puse como si fuese mojito
a += "(COCKTAILS)-[A25:IS_A]->(BEVERAGE),(COCKTAILS)-[B25:USE]->(LEMON),(COCKTAILS)-[C25:USE]->(SUGAR),"
a += "(COCKTAILS)-[D25:TASTE]->(SWEET),"

#Shushii Relationships
a += "(SUSHI)-[A26:IS_A]->(MAINCOURSE),(SUSHI)-[B26:USE]->(SALMON),(SUSHI)-[C26:USE]->(TOMATO),"
a += "(SUSHI)-[D26:TASTE]->(SALTY)"

engine = a
session.run(engine)

db.close()