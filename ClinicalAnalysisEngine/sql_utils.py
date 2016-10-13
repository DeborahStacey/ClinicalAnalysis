## Class: Sql
# Primary Owner: Russell Dunk

import psycopg2


def get_all():
    con = psycopg2.connect(
        "dbname='postgres'\
        user='postgres'\
        host='159.203.6.218'\
        port='5432' \
        password='eightgravity'")
    cur = con.cursor()
    cur.execute("""SELECT * FROM wellcat""")
    return cur.fetchall()

def get_by_name(name):
    con = psycopg2.connect(
        "dbname='postgres'\
        user='postgres'\
        host='159.203.6.218'\
        port='5432' \
        password='eightgravity'")
    cur = con.cursor()
    cur.execute("""SELECT * FROM wellcat WHERE name = 'name'""")

def get_by_id(id):
    con = psycopg2.connect(
        "dbname='postgres'\
        user='postgres'\
        host='159.203.6.218'\
        port='5432' \
        password='eightgravity'")
    cur = con.cursor()
    cur.execute("""SELECT * FROM wellcat WHERE id = 'id'""")
