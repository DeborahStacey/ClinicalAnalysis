## Class: Sql
# Primary Owner: Russell Dunk

import psycopg2

# pet, animal, breed, gender are the dbs we have read access to
def get_all():
    con = psycopg2.connect(
        "dbname='WelcatWorking'\
        user='welcatreaders'\
        host='welcat-working.cz3evk2oqbiz.us-west-2.rds.amazonaws.com'\
        port='5432' \
        password='ThatBackendTho'")
    cur = con.cursor()
    cur.execute("""SELECT * FROM gender""")
    return cur.fetchall()

