## Class: Sql
# Primary Owner: Russell Dunk

import psycopg2
from psycopg2.extras import RealDictCursor

# pet, animal, breed, gender are the dbs we have read access to

def get_con():
    return psycopg2.connect(
        "dbname='WelcatWorking'\
        user='welcatreaders'\
        host='http://cat.ddns.net/'\
        port='5432' \
        password='ThatBackendTho'")

def get_all():
    cur = get_con().cursor()
    cur.execute("""SELECT * FROM pet""")
    return cur.fetchall()


def get_dict(query):
    cur = get_con().cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(query)
    return cur.fetchall()
