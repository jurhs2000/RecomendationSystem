from flask import g
from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver('bolt://localhost',auth=basic_auth("neo4j", "uvg123"), encrypted=False)

def get_db():
    if not hasattr(g, 'neo4j_db'):
        g.neo4j_db = driver.session()
    return g.neo4j_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'neo4j_db'):
        g.neo4j_db.close()